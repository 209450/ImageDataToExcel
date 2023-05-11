from PIL import Image


def crop_image_by_rectangle_coordinates_with(input_file_path, table_rectangles):
    input_image = Image.open(input_file_path)
    cropped_images_of_tables = []
    for table_rectangle in table_rectangles:
        x1, y1 = table_rectangle.top_left
        x2, y2 = table_rectangle.bottom_right

        image_of_excel_table = input_image.crop((x1, y1, x2, y2))
        cropped_images_of_tables.append(image_of_excel_table)

    # for image_of_excel_table in images_of_excel_table:
    #     image_of_excel_table.show()

    return cropped_images_of_tables


