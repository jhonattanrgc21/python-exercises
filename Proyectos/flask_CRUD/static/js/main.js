const btndelete = document.querySelectorAll('.btn-delete');

if(btndelete)
{
    btnArray = Array.from(btndelete)
    btnArray.forEach((btn) => {
        btn.addEventListener('click', e => {
            if(!confirm('Desea eliminar este contacto?'))
                e.preventDefault();
        })
    })
}