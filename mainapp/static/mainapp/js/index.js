const callButton = document.getElementById("callButton");
const closeModalButton = document.getElementById("closeModal")
const modal = document.getElementById("modal");


callButton.addEventListener("click", () => {
    modal.hidden = false;
})

closeModalButton.addEventListener("click", () => {
    modal.hidden = true;
})