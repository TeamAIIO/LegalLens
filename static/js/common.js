
function callLaywer(url, contentId, answerId) {
    const answerEl = document.getElementById(answerId)

    getAnswer(url, contentId).then(res => {
        console.log('res!!!!', res)
        answerEl.innerHTML = 'JSON:' + JSON.stringify(res)
    }).catch((error) => {
        alert('답변 중 오류가 발생했습니다.')
        console.error(error)
    });;
}


function getAnswer(url, contentId) {

    const contents = document.getElementById(contentId).value
    const jsonData = {'input': contents}

    return new Promise((resolve, reject) => {
        let xhr = new XMLHttpRequest();
        xhr.open('POST', url, true);
        // xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        // xhr.send();
        xhr.setRequestHeader('Content-Type', 'application/json')
        xhr.send(JSON.stringify(jsonData))

        xhr.onload = function () {
        if (xhr.status == 200) {
            //success 
            // console.log(xhr.response)
            const result = JSON.parse(xhr.response)
            resolve(result)
        } else {
            //failed
            // console.log('error', xhr)
            const result = JSON.parse(xhr.response)
            reject(result)
        }
        };
    });
}

