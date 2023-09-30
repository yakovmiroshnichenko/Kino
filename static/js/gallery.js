
const addMoreBtn = document.getElementById('add-more')
const totalNewForms = document.getElementById('id_form-__prefix__-image')
addMoreBtn.addEventListener('click', add_new_form)

function add_new_form(event) {
    if (event) {
        event.preventDefault()
    }
    const totalGalleryImages = document.getElementsByClassName('galleryItemWrapper')
    const currentFormCount = totalGalleryImages.length // + 1
    const formCopyTarget = document.getElementById('image-list')
    const copyEmptyFormEl = document.getElementById('empty-form').cloneNode(true)
    copyEmptyFormEl.setAttribute('class', 'galleryItemWrapper')
    copyEmptyFormEl.setAttribute('id', `form-${currentFormCount}`)
    const regex = new RegExp('__prefix__', 'g')
    copyEmptyFormEl.innerHTML = copyEmptyFormEl.innerHTML.replace(regex, currentFormCount)
    totalNewForms.setAttribute('value', currentFormCount + 1)
    formCopyTarget.append(copyEmptyFormEl)
}
// Получить элемент предварительного отображения
upload.style.display