
const addMoreBtn = document.getElementById('add-more')
addMoreBtn.addEventListener('click', add_new_form)

function add_new_form(event) {
    if (event) {
        event.preventDefault()
    }
    const formCopyTarget = document.getElementById('image-list')
    const emptyFormEl = document.getElementById('empty-form').cloneNode(true)
    emptyFormEl.setAttribute('class', 'galleryItemWrapper')
    formCopyTarget.append(emptyFormEl)
}
