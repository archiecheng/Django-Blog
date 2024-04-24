$(function () {
    function bindCaptchaBtnClick() {
        $("#captcha-btn").click(function (event) {
            let $this = $(this);
            let email = $("input[name='email']").val();
            if (!email) {
                alert("Please enter email");
                return;
            }
            // Cancel button click event
            $this.off('click');
            // Send ajax request
            $.ajax('/auth/captcha?email='+email, {
                method: 'GET',
                success: function(result){
                    if(result['code'] == 200){
                        alert("Send Captcha Code successfully! ");
                    }else{
                        alert(result['message']);
                    }
                },
                fail: function (error){
                    console.log(error);
                }
            })
            // Countdown
            let countdown = 10;
            let timer = setInterval(function () {
                if (countdown <= 0) {
                    $this.text('get verification code');
                    // clear timer
                    clearInterval(timer);
                    // Rebind click event
                    bindCaptchaBtnClick();
                } else {
                    countdown--;
                    $this.text(countdown + "s")

                }
            }, 1000)
        })
    }

    bindCaptchaBtnClick();
})