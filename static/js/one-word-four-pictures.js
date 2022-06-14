const imageGroupContainer = [
    item1 = {
        id: 'banking',
        content: {
            src1: 'https://images.unsplash.com/photo-1601597111158-2fceff292cdc?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8YmFua3xlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
            src2: 'https://images.unsplash.com/photo-1582139329536-e7284fece509?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTB8fGJhbmt8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src3: 'https://images.unsplash.com/photo-1551260627-fd1b6daa6224?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjB8fGJhbmt8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src4: 'https://images.unsplash.com/photo-1607944024060-0450380ddd33?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTF8fGJhbmt8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
        },
    },
    item2 = {
        id: 'children',
        content: {
            src1: 'https://images.unsplash.com/photo-1603354350317-6f7aaa5911c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8a2lkcyUyMGxlYXJuaW5nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
            src2: 'https://images.unsplash.com/photo-1603354350317-6f7aaa5911c5?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8a2lkcyUyMGxlYXJuaW5nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
            src3: 'https://images.unsplash.com/photo-1565350831386-8c52421af9fa?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8a2lkcyUyMGxlYXJuaW5nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
            src4: 'https://images.unsplash.com/photo-1565350831386-8c52421af9fa?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8a2lkcyUyMGxlYXJuaW5nfGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
        },
    },
    item3 = {
        id: 'currency',
        content: {
            src1: 'https://images.unsplash.com/photo-1579621970588-a35d0e7ab9b6?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OXx8bW9uZXl8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src2: 'https://images.unsplash.com/photo-1459257831348-f0cdd359235f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTN8fG1vbmV5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
            src3: 'https://images.unsplash.com/photo-1579621970563-ebec7560ff3e?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTJ8fG1vbmV5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
            src4: 'https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MjN8fGN1cnJlbmN5fGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
        },
    },
    item4 = {
        id: 'religion',
        content: {
            src1: 'https://images.unsplash.com/photo-1601921209216-60811afbc245?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mnx8cmVsaWdpb258ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src2: 'https://images.unsplash.com/photo-1528357136257-0c25517acfea?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8cmVsaWdpb258ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src3: 'https://images.unsplash.com/photo-1578301978162-7aae4d755744?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8cmVsaWdpb258ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src4: 'https://images.unsplash.com/photo-1504052434569-70ad5836ab65?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fHJlbGlnaW9ufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
        },
    },
    item5 = {
        id: 'car',
        content: {
            src1: 'https://images.unsplash.com/photo-1552642762-f55d06580015?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8dmVoaWNsZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
            src2: 'https://images.unsplash.com/photo-1612477257392-7eaf635ab744?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MTh8fHZlaGljbGV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src3: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8YWlycGxhbmV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src4: 'https://images.unsplash.com/photo-1463567517034-628c51048aa2?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8OHx8c2hpcHxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
        },
    },
    item6 = {
        id: 'home',
        content: {
            src1: 'https://images.unsplash.com/photo-1586023492125-27b2c045efd7?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NXx8aG9tZXxlbnwwfHwwfHw%3D&auto=format&fit=crop&w=500&q=60',
            src2: 'https://images.unsplash.com/photo-1648737965772-b3385bfce64f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDF8MHxzZWFyY2h8MjN8fGhvbWV8ZW58MHx8MHx8&auto=format&fit=crop&w=500&q=60',
            src3: 'https://images.unsplash.com/photo-1646059159273-c6caf7be0475?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8N3x8ZGVufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
            src4: 'https://images.unsplash.com/photo-1558369345-7db513bb1a1c?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8NHx8ZGVufGVufDB8fDB8fA%3D%3D&auto=format&fit=crop&w=500&q=60',
        },
    },
]
const outputValuesContainer = document.querySelector('.output-values-container');
const inputValuesContainer = document.querySelector('.input-values-container');
function loadGame () {
    function getRandomValue (num) {
        return Math.floor(Math.random() * (num));
    }

    function getRandomValues (num) {
        let imageGroupContent = [];
        while (imageGroupContent.length < num) {
            let randNum = getRandomValue(num);
            if (imageGroupContent.indexOf(randNum) === -1) {
                imageGroupContent.push(randNum);
            }
        }
        return imageGroupContent;
    }
    const imageGroup = document.querySelector('.image-group');
    let imageGroupId = imageGroup.id;
    console.log(imageGroupId);
    console.log(`This is image-group ID: ${imageGroupId}`);

    let imageGroupArray = getRandomValues(imageGroupContainer.length);
    console.log(imageGroupArray);

    let currentImageGroupContent = getRandomValue(imageGroupContainer.length);

    console.log(imageGroupContainer[currentImageGroupContent].id)
    imageGroup.setAttribute('id', `${imageGroupContainer[currentImageGroupContent].id}`);
    imageGroupId = imageGroup.id;
    console.log(imageGroupId);
    const imageGroupIdLength = imageGroup.id.length;
    for (const currentContent in imageGroupContainer[currentImageGroupContent].content) {
        imageGroup.innerHTML += `
                                <div class="border border-red-700 rounded-lg hover:scale-[.99]">
                                    <img class="rounded-lg border border-pink-700" src="${imageGroupContainer[currentImageGroupContent].content[currentContent]}" alt="">
                                </div>
                            `
    }
    
    let imageGroupBtnsContent = getRandomValues(imageGroupIdLength);
    imageGroupBtnsContent.forEach((content) => {
        outputValuesContainer.innerHTML += `
                                    <div class="output bg-rose-400 text-gray-100 h-10 w-10 flex items-center justify-center rounded-lg"></div>
                                `;
        inputValuesContainer.innerHTML += `
                                    <button class="input shadow-lg uppercase border-2 border-rose-500 hover:scale-[.99] bg-white text-rose-500 h-8 w-8 md:h-10 md:w-10 xl:h-12 xl:w-12 flex items-center justify-center rounded-lg">${imageGroupId.charAt(content)}</button>
                                `;
    })

    const inputs = document.querySelectorAll('.input');
    inputs.forEach((input) => {
    input.addEventListener('click', (e) => {
        makeEntries(e.currentTarget.textContent, outputValuesContainer);
    })
})
}
window.addEventListener('load', loadGame);

const modifyEntriesBtn = document.querySelectorAll('.modify-entries');
modifyEntriesBtn.forEach((btn) => {
    btn.addEventListener('click', (e) => {
        if (e.currentTarget.classList.contains('del-entries')) {
            delEntries(outputValuesContainer);
        } else if (e.currentTarget.classList.contains('submit-entries')) {
            submitEntries(outputValuesContainer);
        } else if (e.currentTarget.classList.contains('clear-entries')) {
            clearEntries(outputValuesContainer);
        } else {}
    })
});


console.log('Window Loaded');

function getOutputValues (arg1) {
    outputValuesArray = [];
    const outputValues = arg1.querySelectorAll(`.output`);
    outputValues.forEach((arg) => {
        outputValuesArray.push(arg.textContent);
    })
    return outputValuesArray;
}

function delEntries (arg1) {
    const outputValuesContent = getOutputValues(arg1);
    outputValuesContent.pop();
    let counter = 0;
    const outputValues = arg1.querySelectorAll('.output');
    let outputValuesBeforeFilter = [];
    outputValues.forEach((value) => {
        outputValuesBeforeFilter.push(value);
    });
    let outputValuesAfterFilter = outputValuesBeforeFilter.filter((value) => value.textContent != '');
    outputValues.forEach((arg) => {
        if (counter < outputValuesAfterFilter.length-1) {
            arg.textContent = outputValuesContent[counter];
        } else if (counter === outputValuesAfterFilter.length-1) {
            console.log('Hello');
            arg.textContent = '';
        }
        counter++;
    })
}

function makeEntries (arg1, arg2) {
    let outputValues = arg2.querySelectorAll('.output');
    let outputValuesContent = getOutputValues(arg2);
    outputValuesContent = outputValuesContent.filter((value) => value.length >= 1);
    outputValuesContent.push(arg1);
    console.log(outputValuesContent);
    let counter = 0;
    outputValuesContent.forEach((value) => {
        if (counter <= outputValuesContent.length-1) {
            outputValues[counter].textContent = value;
        } else {
            console.log(value);
        }
        counter++;
    })
}

function submitEntries (arg1) {
    const outputValuesContent = getOutputValues(arg1);
    let someValue = '';
    outputValuesContent.forEach((value) => {
        someValue += value;
    });
    let imageGroupId = document.querySelector('.image-group').id;
    if (someValue === imageGroupId) {
        console.log('Correct!');
        swal("Good job!", "You clicked the button!", "success");

    } else {
        swal("Wrong!", "Try Again!", "error");
    }
    console.log(someValue);
    console.log(someValue.length);
}

function clearEntries (arg1) {
    arg1.querySelectorAll('.output').forEach((thisTarget) => {
        thisTarget.textContent = '';
    })
}