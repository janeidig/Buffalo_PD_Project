function getData() {
  ajaxGetRequest("/pieChart", pieChart);
  ajaxGetRequest("/barGraph", barGraph);
}

//function creating pie chart and adding to div
function pieChart(response) {
  let data = JSON.parse(response);
  let piedata = [{
    values: data,
    labels: ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday","Saturday","Sunday"],
    type: "pie",
  }];
  let layout = {title:"Buffalo PD Incidents By Day of Week"}
  let newPlot = Plotly.newPlot("pieChart", piedata, layout)
  let pieDiv = document.getElementById("pieChart");
  pieDiv["innerhtml"] = newPlot
}

//functions creating bar graph and adding to div
function years(map){
  let xvalues = []
  for (let k of Object.keys(map)){
    xvalues.push(k)
  }return xvalues
}

function incidents(map){
  let yvalues = []
  for (let k of Object.values(map)){
    yvalues.push(k)
  }return yvalues
}

function barGraph(response) {
  let bardata = JSON.parse(response);
  let data = [{
    x: years(bardata),
    y: incidents(bardata),
    type: "bar",
  }];
  let layout = {
  xaxis: {title: 'Year'},
  yaxis: {title: '# of Incidents'},
  barmode: 'relative',
  title: 'Buffalo PD Incidents per Year'
};
  let newPlot = Plotly.newPlot("barGraph", data, layout)
  let barDiv = document.getElementById("barGraph");
  barDiv["innerhtml"] = newPlot
}

//functions creating line chart and posting in div

function lineChart(response) {
  let linedata = JSON.parse(response);
  console.log(linedata)
  newx = [];
  newy = [];
  for (let x of Object.keys(linedata)) {
    newx.push(x)
  }for (let y of Object.values(linedata)) {
    newy.push(y)
  }
  let data = [{
    x: newx,
    y: newy,
    type: "line",
  }];
    let layout = {title:"Number of Incidents at " + String(document.getElementById("line").value)+" Hundred Hours", 
  xaxis: {
    showgrid: false,
    title: {
      text: 'Years',
    }},
  yaxis: {
    title: {
      text: 'Incidents',}}}
  let newPlot = Plotly.newPlot("lineChart", data, layout)
  let lineDiv = document.getElementById("lineChart");
  lineDiv["innerhtml"] = newPlot
}

//function receiving hour from client and calling function to generate line chart

function getLineChart() {
  let hour = document.getElementById("line").value;
  let data = {"line":hour};
  let JSONdata = JSON.stringify(data)
  ajaxPostRequest("/lineChart", JSONdata, lineChart);
}