$(document).ready(function() {
    var dt_table = $('table').DataTable({
        fixedHeader: true,
        order: [[ 0, "desc" ]],
        lengthMenu: [[20 ,50,100,200], [20,50,100,200]],
        columnDefs: [
            {orderable: true,
             searchable: true,
             className: "center",
             targets: [0,5]
            }
        ],
        searching: true,
        processing: true,
        serverSide: true,
        stateSave: true,
        ajax: USERS_LIST_JSON_URL,

        "scrollY":        "400px",
        "scrollCollapse": true,
        "paging":         false
        
        
        
    });    


    setInterval( function () {
        dt_table.ajax.reload();
    }, 5000 );
    
    
});