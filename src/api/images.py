import os
import shutil
import json

from fastapi import APIRouter, UploadFile, Query

from src.api.dependencies import DBDep
from src.exceptions.base import AllreadyExistsException
from src.exceptions.images import ImagesAllreadyExistsHTTPException
from src.schemas.images import ImageAdd
from src.tasks.tasks import resize_image


router = APIRouter(prefix='/images', tags=['Изображения'])


@router.post("", summary="Загрузить изображение")
async def upload_image(
    file: UploadFile,
    db: DBDep,
    route_page: str = Query(
        description="route, с которого запрошена загрузка файла",
        example="articles"
    ),
    name: str = Query(
        description="человеческое название, для чего загружается изображение",
        example="статья 1"
    )
):
    image_folder = f"src/static/images/{route_page}"
    print(f"{image_folder = }")
    if not os.path.exists( image_folder ):
        os.makedirs( image_folder )
        print(f"Создано: {image_folder}")

    image_path = f"{image_folder}/{file.filename}"
    image_data = ImageAdd(
        name=name,
        path=image_path,
    )

    try:
        await db.images.add( image_data )
        await db.commit()
    except AllreadyExistsException as exc:
        raise ImagesAllreadyExistsHTTPException

    with open(image_path, "wb+") as new_file:
        shutil.copyfileobj(file.file, new_file)

    result = resize_image.delay(
        image_path = image_path,
        output_folder = image_folder
    )

    images_data = [ImageAdd( name=f"{name} - {k}px", path=v) for k, v in json.loads( result.get() ).items()]
    try:
        await db.images.add_bulk( images_data )
        await db.commit()
    except AllreadyExistsException as exc:
        raise ImagesAllreadyExistsHTTPException





