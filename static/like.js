const likeButtons = document.querySelectorAll(".like-button");
var id = likeButtons.length;
for (const button of likeButtons) {
    const entryNumber = id;
    button.addEventListener("click", () => {
        const url = `/entries/${entryNumber}/like`;
        fetch(url, {
            method: "post"
        })
            .then(response => response.json())
            .then(data => {
                button.innerText = `+ ${data.likes}`;
            })
    });
    id -= 1;
}