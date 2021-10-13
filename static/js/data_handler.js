export let dataHandler = {

    _data: {},

    _api_post: function(url, data) {
        return new Promise ((resolve, reject) => {
            fetch(url, {
                method: 'POST',
                headers: {
                    contentType: 'application/json'
                },
                body: JSON.stringify(data)
            })
                .then(res => res.json())
                .then(data => resolve(data))
                .catch(err => reject(err))
        })
    },
}
