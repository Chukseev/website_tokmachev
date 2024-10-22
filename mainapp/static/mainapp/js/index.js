import {initFetchForm, resetForm} from "./fetchForm.js";

const callButton = document.getElementById("callButton");
const closeModalButton = document.getElementById("closeModal")
const modal = document.getElementById("modal");
const modalContent = document.getElementById("modalContent");
const modalBody = document.querySelector(".modal__body");
const callForm = document.getElementById('callForm');

modal.addEventListener("click", () => {
    modal.hidden = true;
    resetForm();
})

modalContent.addEventListener("click", (event) => {
    event.stopPropagation();
})

callButton.addEventListener("click", () => {
    modal.hidden = false;
})

closeModalButton.addEventListener("click", () => {
    modal.hidden = true;
    resetForm();
})


initFetchForm();