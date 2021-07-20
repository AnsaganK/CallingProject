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

async function getPatientInfo(patientId){
    let url = `/api/patient/${patientId}`;
    let patient_block = document.getElementById('patient_detail_card');
    patient_block.style = 'display:flex;margin-top:25px;flex-direction:column;';
    patient_block.innerHTML = preloader;
    let more_button = document.getElementById(`more_button_${patientId}`);
    more_button.classList.toggle('is-loading');
    more_button.classList.toggle('disabled');
    await fetch(url).then(async response => {
                  if (response.status === 200) {
                    generatePatientInfo(await response.json());
                  } else {
                      console.log(response.status);
                      throw new Error(response.status);
                  }
                  more_button.classList.toggle('is-loading');
                  more_button.classList.toggle('disabled');
            }).catch(
                 (error) => {
                     more_button.classList.toggle('is-loading');
                     more_button.classList.toggle('disabled');
                     console.log(error);
                 }
             );
}



function generatePatientInfo(patient){
    let father = patient.father;
    let patient_block = document.getElementById('patient_detail_card');
    let father_info = father !== null ? `
    <div>
        <span>
            ФИО:
        </span>
        <span>
            ${father.last_name} ${father.first_name} ${father.patronymic}
        </span>
    </div>
    <div>
        <span>
            Группа крови:
        </span>
        <span>
            ${father.blood_type}
        </span>
    </div>
    <div>
        <span>
            Характер производства:
        </span>
        <span>
            ${father.work_type}
        </span>
    </div>
    <div>
        <span>
            Вредные привычки:
        </span>
        <span>
            ${father.bad_habits}
        </span>
    </div>
    <div>
        <span>
            Комментарии:
        </span>
        <span>
            ${father.comments}
        </span>
    </div>
    ` : '';
    let patient_info = `
<div class="user-info">
        <span class="user-info-title">Основная информация</span>
        <div>
            <span>
                ФИО:
            </span>
            <span>
                ${patient.last_name}
                ${patient.first_name}
                ${patient.patronymic}
            </span>
        </div>
        <div>
            <span>
                Дата рождения:
            </span>
            <span>
                ${patient.birth_date}
            </span>
        </div>
        <div>
            <span>
                Вес до беременности:
            </span>
            <span>
                ${patient.before_weight}
            </span>
        </div>
        <div>
            <span>
                Рост:
            </span>
            <span>
                ${patient.height}
            </span>
        </div>
        <div>
            <span>
                Группа крови:
            </span>
            <span>
                ${patient.blood_type}
            </span>
        </div>
        <div>
            <span>
                Кол-во детей:
            </span>
            <span>
                ${patient.children_amount}
            </span>
        </div>
        <div>
            <span>
                ПМСП:
            </span>
            <span>
                ${patient.PMSP}
            </span>
        </div>
        <div>
            <span>
                ИИН:
            </span>
            <span>
                ${patient.IIN}
            </span>
        </div>
        <div>
            <span>
                Район:
            </span>
            <span>
                ${patient.district}
            </span>
        </div>  
        <div>
            <span>
                Адрес:
            </span>
            <span>
                ${patient.address}
            </span>
        </div>
        <div>
            <span>
                Место работы:
            </span>
            <span>
                ${patient.work_type}
            </span>
        </div>
        <div>
            <span>
                Всего беременностей:
            </span>
            <span>
                ${patient.total_pregnancies}
            </span>
        </div>
        <span class="user-info-title">Группа риска</span>
        <div>
            <span>
                Перенесенные заболевания:
            </span>
            <span>
                ${patient.past_illnesses}
            </span>
        </div>
        <div>
            <span>
                Сопутсвующие заболевания:
            </span>
            <span>
                ${patient.accompanying_illnesses}
            </span>
        </div>
        <div>
            <span>
                Группа риска:
            </span>
            <span>
                ${patient.risk_group}
            </span>
        </div>
        <div>
            <span>
                Вредные привычки:
            </span>
            <span>
                ${patient.bad_habits}
            </span>
        </div>
        <span class="user-info-title">Хронологическая сводка</span>
        <div>
            <span>
                Дата взятия:
            </span>
            <span>
                ${patient.registration_date}
            </span>
        </div>
        <div>
            <span>
                ПМ:
            </span>
            <span>
                ${patient.last_menstruation}
            </span>
        </div>
        <div>
            <span>
                Предплогаемая дата родов:
            </span>
            <span>
                ${patient.due_date}
            </span>
        </div>
        <div>
            <span>
                Дата снятия:
            </span>
            <span>
                ${patient.deregistration_date}
            </span>
        </div>
        <div>
            <span>
                Причина снятия:
            </span>
            <span>
                ${patient.deregistration_cause}
            </span>
        </div>
        <div>
            <span>
                Комментарии:
            </span>
            <span>
                ${patient.comments}
            </span>
        </div>
        
        
</div>
    `;
    patient_block.innerHTML = patient_info;
}

function detail_admin_item(id, name){
    let items_text = document.querySelectorAll('.hide');
    for(let i=0; i<items_text.length; i++){
        items_text[i].classList.remove('hide');
        items_text[i].nextElementSibling.innerHTML = '';
    }

    let detail_item_block = document.getElementById(`detail_item_${id}`);
    let detail_text = detail_item_block.previousElementSibling;
    detail_text.classList.add('hide');
    let admin_panel_form = document.getElementById('admin_panel_form');
    let csrf_value = admin_panel_form.children[0].value;
    let csrf_name = admin_panel_form.children[0].name;
    console.log(csrf_value);
    detail_item_block.innerHTML = `
     <form action="" method="post">
            <input type="hidden" name="${csrf_name}" value="${csrf_value}">
            <input type="hidden" name="id" value="${id}">
            <input class="input is-warning" name="name" type="text" placeholder="" value="${name}">
            <div class="buttons">
                <button type="submit" class="button is-primary">Изменить</button>
                <a href="?id=${id}" class="button is-danger">Удалить</a>
            </div> 
     </form>
    `
}