function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// using jQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

$("#login-button").click(function (event) {
    event.preventDefault();

    email = $('input[name=email]').val();
    password = $('input[name=password]').val();
    passwordCheck = $('input[name=passwordCheck]').val();
    name = $('input[name=name]').val();

    if(name.trim() == "") {
        $('input[name=name]').focus();
    } else if (email.trim() == "") {
        $('input[name=email]').focus();
    } else if (password.trim() == "") {
        $('input[name=password]').focus();
    } else if (passwordCheck.trim() == "") {
        $('input[name=passwordCheck]').focus();
    } else {
        if (password === passwordCheck) {
            var csrftoken = getCookie('csrftoken');

            $.ajaxSetup({
                beforeSend: function (xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                    }
                }
            });

            $.post({
                url: '/member/register/',
                dataType: 'json',
                data: {
                    email: email,
                    password: password,
                    name: name
                }
            })
                .done(function (data) {
                    console.log(data.msg)
                    if (data.status == "success") {
                        $('form').fadeOut(500);
                        $('.guest').fadeOut(500);
                        $('.wrapper').addClass('form-success');
                        setTimeout(function () {
                            location.href = "/member/login/"
                        }, 1500)
                    } else {
                        alert(data.msg)
                    }
                })
        } else {
            alert("Password Does Not Match");
            $('input[name=passwordCheck]').focus();
        }
    }
});