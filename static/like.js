entries = document.querySelectorAll(".entry");
let id = 1;
for (entry of entries) {
    likeButton = entry.querySelector(".like-button")
    likeButton.addEventListener("click", () => {
        const url = `entries/${id}/like`;
        fetch(url)
            .then(data => {
                likeButton.innerText = `+ ${entry.likes}`;
            })
    })
    id += 1;
}