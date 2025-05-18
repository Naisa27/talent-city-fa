from time import sleep

from PIL import Image
import os
import json

from src.tasks.celery_app import celery_instance


@celery_instance.task
def test_task():
    sleep(5)
    print("Я молодец!")


@celery_instance.task
def resize_image( image_path: str, output_folder: str ):
    sizes = [1000, 500, 200]
    print(f"{output_folder = }")

    img = Image.open( image_path )
    base_name = os.path.basename( image_path )
    name, ext = os.path.splitext( base_name )

    if not os.path.exists( output_folder ):
        os.makedirs( output_folder )

        print(f"Папка {output_folder} создана.")

    files = {}

    for size in sizes:
        img_resized = img.resize((size, int(img.height * (size / img.width))), Image.Resampling.LANCZOS)
        new_file_name = f"{name}_{size}px{ext}"

        # Формируем имя файла с указанием ширины
        output_path = os.path.join(output_folder, new_file_name)
        files[size] = output_path

        # Сохраняем изображение
        img_resized.save( output_path)

    print(f"Изображение сохранено в следующих размерах: {sizes} в папке {output_folder}.")

    return json.dumps( files )


