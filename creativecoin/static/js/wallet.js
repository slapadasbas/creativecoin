$(document).ready(function(){
    $("#sourceWallet").on('change', function(e){
        var idx = $("#sourceWallet").find(":selected").val()
        $("#balance").val(+$("#balance-"+idx).val())
        validate_balance()
    })

    $("#amount").on("input", function(e){
        var amount = $("#amount").val()
        validate_balance();
    })

    var idx = $("#sourceWallet").find(":selected").val()
    $("#balance").val(+$("#balance-"+idx).val())
    validate_balance()

    function validate_balance(){
        var idx = $("#sourceWallet").find(":selected").val()
        var balance = parseFloat($("#balance-"+idx).val())
        var amount = parseFloat($("#amount").val())

        if (balance < amount) {
            $("#balance-error").html("Insufficient funds")
            $("#submit").prop("disabled", true)
        }
        else if (balance < 100 || amount < 100){
            $("#balance-error").html("Minimum transfer is 100 CCN")
            $("#submit").prop("disabled", true)
        }
        else {
           $("#balance-error").html("&nbsp;")
            $("#submit").prop("enabled", true)
        }
    }

})

$(".copy").on("click", function(e){
    e.preventDefault();
    var text = $("#ref-code").select();
    document.execCommand("copy");
});

$(".copy2").on("click", function(e){
    e.preventDefault();
    var text = $("#wallet-code").select();
    document.execCommand("copy");
});

$("#receive-btn").on("click", function(e){
    $("#receive-modal").modal({show: true})
})

$("#send-btn").on("click", function(e){
    $("#send-modal").modal({show: true})
})

$("#receive-close").on("click", function(e){
    $("#receive-modal").modal('hide')
})

$("#send-close").on("click", function(e){
    $("#send-modal").modal('hide')
})

$("#send-close2").on("click", function(e){
    $("#send-modal").modal('hide')
})
