document.addEventListener('DOMContentLoaded', () => {

    const dcs = (selectorName) =>  document.querySelector(selectorName)
    const openCloseForm = (selector, type) => selector.addEventListener('click', () => form.style.display = type)

    const form = dcs('#QuestionForm')
    const button = dcs('#QuestionButton')
    const form_close_button = dcs('#CloseFormButton')
    const form_blur = dcs('.form__item__blur')

    openCloseForm(button, 'flex')
    openCloseForm(form_blur, 'none')
    openCloseForm(form_close_button, 'none')

    form.addEventListener('submit', (e) => {
        e.preventDefault()

        let all_fields = form.querySelectorAll('input')
        let send_status = true

        all_fields.forEach(field => {
            if (field.value.length < 3 || field.value == null) {
                send_status = false
            }
        })

        if (!send_status) {
            createMessage(dcs('#FieldsIsEmpty').value)
            return ''
        }

        if (confirm(dcs('#ConfirmSend').value)) {
            const formData = new FormData(form)
            fetch(`/api/question-create/`, {
                method: "POST",
                body: formData
            })
                .then(res => res.json())
                .then(data => {
                    if (data.status == 'success') {
                        form.style.display = "none"
                        createMessage(dcs('#SentSuccessfully').value)
                    } else {
                        console.log('Error', data)
                        if (data.message == 'You can only submit a question once every half hour.') {
                            createMessage(dcs('#TimesUp').value)
                        } else {
                            createMessage(data.message)
                        }
                    }
                })
        }
    })

    const question_list = document.querySelectorAll('.question')

    question_list.forEach((question) => {
        let btn_open = question.querySelector('.question__footer__open')
        let btn_close = question.querySelector('.question__footer__close')
        let answer = question.querySelector('.question__answer')

        btn_open.addEventListener('click', () => {
            answer.style.display = "flex";
            btn_open.style.display = "none";
            btn_close.style.display = "block";


            setTimeout(() => {
                answer.style.opacity = 1
            }, 300)
        })

        btn_close.addEventListener('click', () => {
            answer.style.opacity = 0
            btn_open.style.display = "block";
            btn_close.style.display = "none";

            setTimeout(() => {
                answer.style.display = "none";
            }, 300)
        })
    })

    function createMessage( message ) {
        const div = document.createElement("div")
        div.classList.add("notification")
        div.innerHTML = message

        document.body.appendChild(div)

        setTimeout(() => {
            div.style.opacity = 0
        }, 4000)

         setTimeout(() => {
            document.body.removeChild(div)
        }, 4300)
    }
})