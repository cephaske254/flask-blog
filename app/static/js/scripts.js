$(document).ready(function () {
    $('.change-photo-btn').click(function () {
        $('#phtChange').slideToggle()
    })

    $('.delPost').click(function(){
        if(confirm('Proceed to delete? This action cannot be undone!')){
            window.location.href = window.location+'/delete'
        }
    })
  
})