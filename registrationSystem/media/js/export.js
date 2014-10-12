$("#submit_export").click(function(){
    var choose = $("#id_classes").val();
    var wish=$("#id_wish").val();
    Dajaxice.home.exportData(exportDataCallBack, {"choose": choose,"wish":wish});
});
function exportDataCallBack(data){
    location.href = data.path;
}
