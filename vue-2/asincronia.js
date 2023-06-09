const getNombre = (idPost) => {
    fetch(`https://jsonplaceholder.typicode.com/posts/${idPost}`)
        .then(res => {
            return res.json()
        })
        .then(post => {
            console.log(post.id);
            console.log(post.title);
            fetch(`https://jsonplaceholder.typicode.com/users/${post.userId}`)
                .then(res => {
                    return res.json();
                })
                .then(user => {
                    console.log(user.name);
                    console.log(user.email);
                })
        })
}

getNombre(99);
