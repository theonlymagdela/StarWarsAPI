import {dataHandler} from "./data_handler.js";

export let dom = {
    initPage: function () {
        registration();
        login();
        modalWMultiple('.resBtn',  '.modal-close1', '.modal-closeB');
        modalWSingle('.regBtn', '.modal-close2', '.modal-bg2', '.modal2');
        modalWSingle('.logBtn', '.modal-close3', '.modal-bg3', '.modal3');
        modalWSingle('.outBtn', '.modal-close4', '.modal-bg4', '.modal4');
    },
}

function modalWSingle (button, close, bg, modal) {
    const buttonModal = document.querySelector(button);
    const closeBtn = document.querySelector(close);
    const modalBg = document.querySelector(bg)
    const modalW = document.querySelector(modal)

    buttonModal.addEventListener('click', function () {
        modalBg.style.display = 'block';
        modalW.style.display = 'block';
    })
    closeBtn.addEventListener('click', function () {
        modalBg.style.display = 'none';
    })
}

function modalWMultiple (button, close, close2) {
    const buttonModal = document.querySelectorAll(button);
    const XBtn = document.querySelectorAll(close)
    const closeBtn2 = document.querySelectorAll(close2)

    buttonModal.forEach(openB => {
        openB.addEventListener('click', function (e) {
            const currentBtnId = e.target.dataset.planet;
            const background = document.querySelector(`[id=bg-${currentBtnId}]`);
            const modalWindow = document.querySelector(`[id=${currentBtnId}]`);
            background.style.display = 'block';
            modalWindow.style.display = 'block';
    })
    })

    XBtn.forEach(closeB => {
        closeB.addEventListener('click', function (e) {
            const currentBtnId = e.target.dataset.closed;
            const background = document.querySelector(`[id=bg-${currentBtnId}]`);
            const modalWindow = document.querySelector(`[id=${currentBtnId}]`);
            background.style.display = 'none';
            modalWindow.style.display = 'none';
        })
    })

    closeBtn2.forEach(closeB => {
        closeB.addEventListener('click', function (e) {
            const currentBtnId = e.target.dataset.closed;
            const background = document.querySelector(`[id=bg-${currentBtnId}]`);
            const modalWindow = document.querySelector(`[id=${currentBtnId}]`);
            background.style.display = 'none';
            modalWindow.style.display = 'none';
    })
    })
}

function registration () {
    const regData = document.querySelector('.modal2');
    const mailInput = document.querySelector('.usernameReg');
    const passInput = document.querySelector('.passwordReg');
    const nameInput = document.querySelector('.nameReg');
    const surnameInput = document.querySelector('.surnameReg')
    const loginModal = document.querySelector('.modal-bg2');

    regData.addEventListener('submit', function (e) {
        e.preventDefault();
        dataHandler._api_post("/registration",
            {'mail': mailInput.value,
                  'password': passInput.value,
                  'name': nameInput.value,
                  'surname': surnameInput.value});
        loginModal.style.display = 'none';
        alert("Success!!");
    });
}

function login () {
    const logData = document.querySelector('.modal3');
    const mailInput = document.querySelector('.mailLog');
    const passInput = document.querySelector('.passwordLog');
    const loginModal = document.querySelector('.modal-bg3');

    logData.addEventListener('submit', function (e) {
        e.preventDefault();
        dataHandler._api_post('/login',
            {'mail': mailInput.value,
                  'password': passInput.value},);
        loginModal.style.display = 'none';
        alert("Success!!")
    });
}
