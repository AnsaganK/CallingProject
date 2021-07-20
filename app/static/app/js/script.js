var preloader = `
<div class="loading">
    <div class="loader_wrap">
            <div class="loftloader-wrapper pl-wave">
                <div class="preloader">
                  <span></span>
                </div>
            </div>
    </div>
    <p class="load_text">Данные загружаются</p>
</div>`

function getPatientInfo(patientId){
    let patient_block = document.getElementById('patient_detail');
    patient_block.children[0].style = 'display:flex;margin-top:25px;';
    patient_block.children[0].innerHTML = preloader;
}