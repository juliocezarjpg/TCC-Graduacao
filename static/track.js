const video = document.getElementById("myvideo");
const canvas = document.getElementById("canvas");
const context = canvas.getContext("2d");
let trackButton = document.getElementById("trackbutton");
let updateNote = document.getElementById("updatenote");
let updateStatus = document.getElementById("updatestatus");
let imagem = document.getElementById("img");

let isVideo = false;
let model = null;

const modelParams = {
    flipHorizontal: true,   // flip e.g for video
    maxNumBoxes: 20,        // maximum number of boxes to detect
    iouThreshold: 0.5,      // ioU threshold for non-max suppression
    scoreThreshold: 0.6,    // confidence threshold for predictions.
}

function startVideo() {
    handTrack.startVideo(video).then(function (status) {
        console.log("video started", status);
        if (status) {
            updateNote.innerText = "Video started. Now tracking"
            isVideo = true
            runDetection()
        } else {
            updateNote.innerText = "Please enable video"
        }
    });
}

function toggleVideo() {
    if (!isVideo) {
        updateNote.innerText = "Starting video"
        startVideo();
    } else {
        updateNote.innerText = "Stopping video"
        handTrack.stopVideo(video)
        isVideo = false;
        updateNote.innerText = "Video stopped"
    }
}

function runDetection() {
    fetch('/api/v1/status',{
    method:'GET'})
    .then(response => response.text())
    .then(result => {
        if (result == 1){
            updatestatus.innerText = "Braço ligado!"
        }
        else if (result == 3){
            updatestatus.innerText = "Braço desligado!"
        }
        
    })
    .catch(error => console.log('error', error));

    console.log("Ola")
    fetch("https://tcc-julio.herokuapp.com/api/v1/img_download",
    {method:'GET'})
    .then(response => response.text())
    .then(result => {
        console.log("Tudo")
        //image.src = result
        console.log(result)
    })
    .catch(error => console.log('error', error));
            
    model.detect(video).then(predictions => {
        if (predictions.length > 0){
          const data = {"X": predictions[0].bbox[0],
                        "Y":predictions[0].bbox[1],
                        "Area":parseFloat(predictions[0].bbox[2])*parseFloat(predictions[0].bbox[3])}
          console.log(data);
          fetch('/api/v1/data_upload',{
            method:'POST',
            headers: {
                      'Accept': 'application/json',
                      'Content-Type': 'application/json'
                    },
            body: JSON.stringify(data)
          })
          model.renderPredictions(predictions, canvas, context, video);
        }
        if (isVideo) {
            requestAnimationFrame(runDetection);
        }
    });
}

// Load the model.
handTrack.load(modelParams).then(lmodel => {
    // detect objects in the image.
    model = lmodel
    updateNote.innerText = "Loaded Model!"
    trackButton.disabled = false
});