$("#submit_export").click(function(){
    var choose = $("#id_classes").val();
    Dajaxice.home.exportData(exportDataCallBack, {"choose": choose});
});
function exportDataCallBack(data){
    location.href = data.path;
}
