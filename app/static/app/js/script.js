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

function reformat_object(object){
    if(object.constructor === Object){
        return object.name
    }else if(Array.isArray(object)){
        let data = '';
        object.forEach(
            elem => {
                data += `<span>${elem.name}</span><br>`
            }
        )
        return data;
    }else {
        return object
    }
}

function isNull(object){
    return object === null || object === '' || object.length === 0 ? '-' : reformat_object(object);
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
                ${isNull(patient.birth_date)}
            </span>
        </div>
        <div>
            <span>
                Вес до беременности:
            </span>
            <span>
                ${isNull(patient.before_weight)}
            </span>
        </div>
        <div>
            <span>
                Рост:
            </span>
            <span>
                ${isNull(patient.height)}
            </span>
        </div>
        <div>
            <span>
                Группа крови:
            </span>
            <span>
                ${isNull(patient.blood_type)}
            </span>
        </div>
        <div>
            <span>
                Кол-во детей:
            </span>
            <span>
                ${isNull(patient.children_amount)}
            </span>
        </div>
        <div>
            <span>
                ПМСП:
            </span>
            <span>
                ${isNull(patient.PMSP)}
            </span>
        </div>
        <div>
            <span>
                ИИН:
            </span>
            <span>
                ${isNull(patient.IIN)}
            </span>
        </div>
        <div>
            <span>
                Район:
            </span>
            <span>
                ${isNull(patient.district)}
            </span>
        </div>  
        <div>
            <span>
                Адрес:
            </span>
            <span>
                ${isNull(patient.address)}
            </span>
        </div>
        <div>
            <span>
                Место работы:
            </span>
            <span>
                ${isNull(patient.work_type)}
            </span>
        </div>
        <div>
            <span>
                Всего беременностей:
            </span>
            <span>
                ${isNull(patient.total_pregnancies)}
            </span>
        </div>
        <span class="user-info-title">Группа риска</span>
        <div>
            <span>
                Перенесенные заболевания:
            </span>
            <span>
                ${isNull(patient.past_illnesses)}
            </span>
        </div>
        <div>
            <span>
                Сопутсвующие заболевания:
            </span>
            <span>
                ${isNull(patient.accompanying_illnesses)}
            </span>
        </div>
        <div>
            <span>
                Группа риска:
            </span>
            <span>
                ${isNull(patient.risk_group)}
            </span>
        </div>
        <div>
            <span>
                Вредные привычки:
            </span>
            <span>
                ${isNull(patient.bad_habits)}
            </span>
        </div>
        <span class="user-info-title">Хронологическая сводка</span>
        <div>
            <span>
                Дата взятия:
            </span>
            <span>
                ${isNull(patient.registration_date)}
            </span>
        </div>
        <div>
            <span>
                ПМ:
            </span>
            <span>
                ${isNull(patient.last_menstruation)}
            </span>
        </div>
        <div>
            <span>
                Предплогаемая дата родов:
            </span>
            <span>
                ${isNull(patient.due_date)}
            </span>
        </div>
        <div>
            <span>
                Дата снятия:
            </span>
            <span>
                ${isNull(patient.deregistration_date)}
            </span>
        </div>
        <div>
            <span>
                Причина снятия:
            </span>
            <span>
                ${isNull(patient.deregistration_cause)}
            </span>
        </div>
        <div>
            <span>
                Комментарии:
            </span>
            <span>
                ${isNull(patient.comments)}
            </span>
        </div>
        
        
</div>
    `;
    patient_block.innerHTML = patient_info;
}

function detail_admin_item(id, name){
    name = name.toString().replaceAll(`"`,'&quot;');
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
    detail_item_block.innerHTML = `
     <form action="" method="post" style="margin: 4px auto">
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


function click_tabs_item(elem){
    let item_id = elem.getAttribute('data-id');
    let block = document.getElementById(`form_block_${item_id}`);
    items_disabled();
    blocks_hide();
    elem.classList.toggle('is-active');
    block.classList.toggle('show_block');
}
function items_disabled(){
    var elems = document.querySelectorAll('.is-active');
    elems.forEach(
        elem => {
            elem.classList.toggle('is-active');
        }
    );
}
function blocks_hide(){
    var elems = document.querySelectorAll('.show_block');
    elems.forEach(
        elem => {
            elem.classList.toggle('show_block');
        }
    );
}


function complaints_field_active(){
    let complaints_field = document.getElementById('complaints_text');
    complaints_field.toggleAttribute('disabled');
}