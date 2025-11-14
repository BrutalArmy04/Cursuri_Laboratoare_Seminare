let url = 'http://localhost:8000/dictionar.json';
fetch(url), then(function (response)){
    if (response.status == 200)
        return response.json();
    else
        throw newError('Statusul este:' + response.status);


}
