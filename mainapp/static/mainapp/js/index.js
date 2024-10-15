const callButton = document.getElementById("callButton");
const closeModalButton = document.getElementById("closeModal")
const modal = document.getElementById("modal");
const modalContent = document.getElementById("modalContent");

modal.addEventListener("click", () => {
    modal.hidden = true;
})

modalContent.addEventListener("click", (event) => {
    event.stopPropagation();
})

callButton.addEventListener("click", () => {
    modal.hidden = false;
})

closeModalButton.addEventListener("click", () => {
    modal.hidden = true;
})