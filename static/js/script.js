var opt = document;
function aluno_matricula(id){
    var aluno = opt.getElementById('dados').aluno.value;
    var matricula = opt.getElementById('dados').matricula.value;

    var _table = opt.querySelector('table');
    
    var newRow = opt.createElement('tr');
    newRow.insertCell(0).innerHTML = aluno;
    newRow.insertCell(1).innerHTML = matricula;

    var input_hidden = opt.createElement('input');
    input_hidden.type = 'hidden';
    input_hidden.name = aluno;
    input_hidden.value = matricula;

    opt.getElementById(id).appendChild(newRow);
    opt.getElementById(id).appendChild(input_hidden);

    newRow.prepend(input_hidden);

    return false;
}

function printWindow(){
    var originalContents = document.body.innerHTML;
    var printReport= document.getElementById('form').innerHTML;
    var printReport2= document.getElementById('table_hw').innerHTML;
    document.body.innerHTML = printReport + printReport2;
    window.print();
    document.body.innerHTML = originalContents;
}

function alertCadastre(){
    alert("Cadastre-se")
}