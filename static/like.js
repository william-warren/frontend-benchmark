// Adds event listener to each like button the call the like view
// with the correct id pass to the arguments
// then updates dom to reflect new data.

const likeButtons = document.querySelectorAll(".like-button");
for (const button of likeButtons) {
    const id = button.dataset["id"];
    button.addEventListener("click", () => {
        const url = `/entries/${id}/like`;
        fetch(url, {
            method: "post"
        })
            .then(response => response.json())
            .then(data => {
                button.innerText = `+ ${data.likes}`;
            })
    });
}