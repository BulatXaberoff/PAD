import matplotlib.pyplot as plt
import numpy as np

def draw_grid(rows, cols, mode='spiral'):
    """
    Рисует прямоугольник, разбитый на подпрямоугольники с раскрашиванием.

    :param rows: Количество делений по вертикали.
    :param cols: Количество делений по горизонтали.
    :param mode: Режим раскраски: 'spiral' или 'snake'.
    """
    # Размеры общего прямоугольника
    width, height = cols, rows

    # Создаем палитру цветов ("радуга")
    colors = plt.cm.rainbow(np.linspace(0, 1, rows * cols))

    # Функция для получения индексов по спирали
    def spiral_indices(rows, cols):
        spiral = []
        left, right, top, bottom = 0, cols - 1, 0, rows - 1
        while left <= right and top <= bottom:
            # Верхняя строка
            for col in range(left, right + 1):
                spiral.append((top, col))
            top += 1

            # Правая колонка
            for row in range(top, bottom + 1):
                spiral.append((row, right))
            right -= 1
            # Нижняя строка
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    spiral.append((bottom, col))
                bottom -= 1

            # Левая колонка
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    spiral.append((row, left))
                left += 1

        return spiral

    # Функция для получения индексов "змейкой"
    def snake_indices(rows, cols):
        snake = []
        for row in range(rows):
            if row % 2 == 0:
                # Слева направо
                for col in range(cols):
                    snake.append((row, col))
            else:
                # Справа налево
                for col in range(cols - 1, -1, -1):
                    snake.append((row, col))
        return snake

    # Получаем индексы в зависимости от режима
    if mode == 'spiral':
        indices = spiral_indices(rows, cols)
    elif mode == 'snake':
        indices = snake_indices(rows, cols)
    else:
        raise ValueError("Unsupported mode. Choose 'spiral' or 'snake'.")

    # Создаем график
    fig, ax = plt.subplots()
    ax.set_xlim(0, width)
    ax.set_ylim(0, height)
    ax.set_aspect('equal')
    ax.axis('off')

    # Рисуем прямоугольники
    color_idx = 0
    for row, col in indices:
        x, y = col, rows - row - 1  # Преобразуем индексы в координаты
        rect = plt.Rectangle((x, y), 1, 1, color=colors[color_idx])
        ax.add_patch(rect)
        color_idx += 1

    plt.show()

# Пример использования
if __name__ == "__main__":
    rows = int(input("Введите количество делений по вертикали: "))
    cols = int(input("Введите количество делений по горизонтали: "))
    mode = input("Введите режим ('spiral' или 'snake'): ").strip()
    draw_grid(rows, cols, mode)
