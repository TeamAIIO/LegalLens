
// 호출
function callLaywer(url, contentId, answerId) {
    const answerEl = document.getElementById(answerId)
    loading(true)

    getAnswer(url, contentId).then(res => {
        console.log('res!!!!', res)
        answerEl.innerHTML = 'JSON:' + JSON.stringify(res)
        loading(false)
    }).catch((error) => {
        alert('답변 중 오류가 발생했습니다.')
        console.error(error)
        loading(false)
    })
}

// api 연결
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
            const result = JSON.parse(xhr.response)
            resolve(result)
        } else {
            //failed
            const result = JSON.parse(xhr.response)
            reject(result)
        }
        };
    });
}

// loading
function loading(isStart) {
    const bodyEl = document.getElementsByTagName('body')[0]

    if(isStart) {
        if(document.getElementById('mask')) return

        const maskHeight = window.document.body.clientHeight;
        const maskWidth  = window.document.body.clientWidth;
        const maskEl = document.createElement('div')
        maskEl.id = 'mask'
        maskEl.style.cssText = 'width:'+ maskWidth +'; height:'+ maskHeight +'; opacity: 0.3; position:absolute; z-index:9000; background-color:#000000; display:none; left:0; top:0;'
    
        const imgPath = '/static/images/loading.gif';
        const loadingEl = document.createElement('img')
        loadingEl.id = 'loadingImg'
        loadingEl.src = imgPath
        loadingEl.style.cssText = 'position: absolute; display: block; margin: 0px auto;'

        bodyEl.append(maskEl)
        maskEl.style.display = 'block'

        maskEl.append(loadingEl)
        loadingEl.style.display = 'block'
    } else {
        const maskEl = document.getElementById('mask')
        maskEl?.remove()
    }
}
 
