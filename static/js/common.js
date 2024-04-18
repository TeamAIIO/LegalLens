
// 호출
function callLaywer(url, contentId, answerId) {
    loading(true)

    // 답변 영역 내용 삭제하고 시작
    const answerEl = document.getElementById(answerId)
    answerEl.replaceChildren()

    getAnswer(url, contentId).then(res => {
        console.log('res!!!!', res)
        // answerEl.innerHTML = 'JSON:' + JSON.stringify(res)
        makeDetailAnswer(res, answerId)
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

// global 임시 선언
let summaryDiv;

// 답변 영역 가공
function makeDetailAnswer(answerData, answerId) {
    const container = document.getElementById(answerId)
    
    const div = document.createElement('div')
    const strong = document.createElement('strong')
    const button = document.createElement('button')
    
    const childDiv = document.createElement('div')
    const small = document.createElement('small')

    strong.textContent = answerData.shortAnswer
    button.textContent = '관련 정보 더보기'
    button.addEventListener('click', () => controlChildContent());
    summaryDiv = childDiv;
    
    childDiv.style.display = 'none'
    small.textContent = answerData.originAnswer

    div.appendChild(document.createElement('hr'))
    div.appendChild(strong);
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createTextNode('- 참조 조문 및 판례'))
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createTextNode('조문)' + replaceBlankText(answerData.referenceArticle)))
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createTextNode('판례)' + replaceBlankText(answerData.referenceCase)))
    div.appendChild(document.createElement('br'))
    div.appendChild(document.createElement('br'))
    div.appendChild(button)

    childDiv.appendChild(document.createTextNode('- 참고 판시사항'))
    childDiv.appendChild(document.createTextNode(answerData.caseNumber))
    childDiv.appendChild(document.createTextNode(' / '))
    childDiv.appendChild(document.createTextNode(formatDate(answerData.date)))
    childDiv.appendChild(document.createElement('br'))
    childDiv.appendChild(small)

    container.appendChild(div)
    container.appendChild(childDiv)
}

// 하단 영역 토글
function controlChildContent() {
    const el = summaryDiv
    console.log('el', el, el?.style.display)

    if(!el) {
        return
    }

    if(el.style.display == 'none') {
        el.style.display = ''
    } else {
        el.style.display = 'none'
    }
}

// 날짜 formatting
function formatDate(inputDate) {
    // string으로 type 고정
    inputDate = typeof inputDate == 'number' ? inputDate.toString() : inputDate

    // 입력된 문자열의 길이가 8이 아니면 유효하지 않음
    if (inputDate.length !== 8) {
        return '0000-00-00'; // 고정값 반환
    }

    // 입력된 문자열을 날짜로 변환
    const year = inputDate.slice(0, 4);
    const month = inputDate.slice(4, 6);
    const day = inputDate.slice(6, 8);
    const date = new Date(`${year}-${month}-${day}`);

    // 날짜가 유효하지 않으면 고정값 반환
    if (isNaN(date.getTime())) {
        return '0000-00-00';
    }

    // "yyyy-mm-dd" 형태로 변환하여 반환
    return `${year}-${month}-${day}`;
}

// 빈 문자열 변환
function replaceBlankText(text) {
    return !Boolean(text) ? '-' : text
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
 
