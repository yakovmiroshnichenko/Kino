// Получить элемент предварительного отображения
const upload = document.getElementById('image-preview');
upload.style.display = 'none'; // Скрыть элемент предварительного отображение

// Получить кнопку "Удалить" по её id
const buttonDelete = document.getElementById("buttonDel");
buttonDelete.addEventListener('click', onButtonClick); // Добавить слушателя события клика на кнопку "Удалить"

// Добавить слушателя события изменения для поля выбора файла
document.getElementById('id_main_image').addEventListener('change', function() {
    const file = this.files[0]; // Получение выбранного файл
    const reader = new FileReader(); // Создание объекта FileReader

    // Функция обратного вызова, выполняющаяся при успешном чтении файла
    reader.onload = function() {
        upload.src = reader.result; // Установка содержимого предварительного отображения
        upload.style.display = 'block'; // Показ предварительного отображения
    }

    // Проверка, был ли выбран файл
    if (file) {
        reader.readAsDataURL(file); // Прочитать файл как Data URL
    } else {
        // Проверка уникальности файла
        upload.src = ''; // Очистить предварительное отображение
        upload.style.display = 'none'; // Скройте его
    }
});

// Функция, выполняемая при клике на кнопку "Удалить"
function onButtonClick() {
    // Очистить поле ввода файла
    const inputFile = document.getElementById('id_main_image');
    inputFile.value = '';

    // Очистить предварительное отображение и скрыть его
    upload.src = '';
    upload.style.display = 'none';
}
// Очистка формы
document.getElementById('clear-form-button').addEventListener('click', function () {
    document.getElementById('film-form').reset();
    onButtonClick()
});
