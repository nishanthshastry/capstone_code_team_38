// fetch('./process.json')
// .then(function(response){
//     return response.json();
// })
// .then(function(data){
//     // document.getElementById("proc_id").innerHTML = '';
    // for(var i=0; i<data.length; i++){
    //     document.getElementById("proc_id").innerHTML += data[i].process_id + '<br />';
    //     document.getElementById("arrt").innerHTML += data[i].arrival + '<br />';
    //     document.getElementById("brt").innerHTML += data[i].burst + '<br />';
    //     document.getElementById("prt").innerHTML += data[i].priority + '<br />';
    // }
// })
// .catch(function(err){
//     console.log(err);
// })

const url = './process.json'
async function getTableData(){
    const response = await fetch(url);
    const data = await response.json();
    // console.log(data);
    for(var i=0; i<data.length; i++){
        document.getElementById("proc_id").innerHTML += data[i].process_id + '<br />';
        document.getElementById("arrt").innerHTML += data[i].arrival + '<br />';
        document.getElementById("brt").innerHTML += data[i].burst + '<br />';
        document.getElementById("prt").innerHTML += data[i].priority + '<br />';
    }
}
getTableData();


const api_url = './calc_res.json';
async function final_res(){
    const response = await fetch(api_url);
    const data = await response.json();
    // console.log(data);
    for(var i=0; i<data.length; i++){
        // console.log(data[i].algo);
        document.getElementById("algos").innerHTML += data[i].algo + '<br />' + '<br />';
        document.getElementById("wt").innerHTML += data[i].avg_wait + '<br />' + '<br />';
        document.getElementById("tat").innerHTML += data[i].avg_tat + '<br />' + '<br />';
    }
    // const algo_names=[];
    // for(var i=0; i<data.length;i++){
        // algo_names.push(data[i].algo);
    // }
    // console.log(algo_names);
}
final_res();

const seq_url = './sequence.json';
async function seq_res(){
    const response = await fetch(seq_url);
    const data = await response.json();
    // console.log(data);
    document.getElementById("seqProcs").innerHTML = '<th>' + 'Process Sequence' + '</th>';
    for(var i=0; i<data.length; i++){
        // console.log(data[i].algo);
        document.getElementById("seqProcs").innerHTML += '<tr>' + '<td>' + data[i].procs + '</td>' + '</tr>';
    }
    
}
seq_res();

var cookie = document.cookie.split(';');

for (var i = 0; i < cookie.length; i++) {

    var chip = cookie[i],
        entry = chip.split("="),
        name = entry[0];

    document.cookie = name + '=; expires=Thu, 01 Jan 1970 00:00:01 GMT;';
}