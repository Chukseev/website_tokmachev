const form = document.getElementById('callForm');
const requestSuccess = document.querySelector('.requestSuccess');
const requestOnError = document.querySelector('.requestOnError');
const modal = document.getElementById("modal");
const modalBody = document.querySelector('.modal__body');

export const initFetchForm = () => {
    form.addEventListener('submit', (event) => {
        event.preventDefault();
        console.log('бибаребух')
        const formData = new FormData(form);
        fetch('', {
            method: 'POST',
            headers: {
                'x-requested-with': 'XMLHttpRequest',
            },
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    form.style.display = 'none';
                    requestSuccess.removeAttribute('hidden');
                }
                else {
                    form.style.display = 'none';
                    requestOnError.removeAttribute('hidden');
                }
                form.reset();
            })
    })
}


export const resetForm = () => {
    form.style.display = 'flex';
    requestSuccess.setAttribute('hidden', true);
    requestOnError.setAttribute('hidden', 'true');
}
