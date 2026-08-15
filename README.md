# emergencias
<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>QUANTUM V3 - RH MATRIX 77</title>
<style>
*{box-sizing:border-box}
body{margin:0;font-family:system-ui;background:#0b1220;color:#e2e8f0;padding:12px;padding-bottom:80px}
.top{display:flex;justify-content:space-between;align-items:center}
h1{font-size:22px;margin:0;color:#22d3ee}
.badge{background:#ef4444;color:#fff;padding:6px 12px;border-radius:20px;font-size:12px;font-weight:800;text-decoration:none}
.card{background:#162032;border-radius:14px;padding:14px;margin:12px 0;border:1px solid #22304a;border-left:4px solid #22d3ee}
.kpi{display:flex;gap:8px}
.kpi div{flex:1;background:#0b1220;padding:10px;border-radius:10px;text-align:center}
.kpi b{display:block;font-size:22px;color:#22d3ee}
input,select{width:100%;padding:14px;border-radius:10px;border:1px solid #2a3a5a;background:#0b1220;color:#fff;margin:6px 0;font-size:16px}
.btn{width:100%;padding:14px;border-radius:10px;border:none;font-weight:800;font-size:15px;margin-top:8px}
.cyan{background:#22d3ee;color:#000}
.amber{background:#fbbf24;color:#000}
.dark{background:#1e293b;color:#fff;border:1px solid #334155}
.item{background:#0b1220;padding:10px;border-radius:8px;margin:6px 0;font-size:13px;border-left:3px solid #22d3ee;display:flex;justify-content:space-between}
</style>
</head>
<body>

<div class="top">
<h1>⚡ QUANTUM V3</h1>
<a class="badge" href="emergencia.html">🚨 EMERGENCIA</a>
</div>
<div style="font-size:11px;color:#64748b;margin-bottom:10px">RH MATRIX 77 - BlackPanter4 - Modo Privado</div>

<div class="card">
<div class="kpi">
<div><b id="asis">0</b>ASIS</div>
<div><b id="fal">77</b>FALTAN</div>
<div><b id="nom">$0</b>NOMINA</div>
</div>
</div>

<div class="card">
<b>CHECADOR</b>
<input id="idEmp" placeholder="ID Ej: AD01 - Cervantes Jose">
<select id="turno"><option>T1 6am-2pm</option><option>T2 2pm-10pm</option><option>T3 10pm-6am</option></select>
<input id="hora" type="time">
<button class="btn cyan" onclick="checar()">✓ CHECAR AHORA</button>
<div id="msg" style="color:#22d3ee;font-size:12px;margin-top:6px"></div>
</div>

<div class="card">
<button class="btn dark" onclick="exportar()">📥 Exportar Asistencia CSV</button>
<button class="btn amber" onclick="generarNomina()">💰 GENERAR NOMINA 77</button>
<div id="status" style="font-size:11px;color:#94a3b8;margin-top:8px"></div>
<div id="lista" style="margin-top:12px"></div>
<div style="margin-top:10px;display:flex;gap:8px"><span onclick="borrar()" style="color:#ef4444;font-size:11px">BORRAR TODO</span><span onclick="location.href='emergencia.html'" style="color:#fbbf24;font-size:11px">Ver emergencias →</span></div>
</div>

<script>
let regs=JSON.parse(localStorage.getItem('quantum_v3')||'[]');
function checar(){
 let id=document.getElementById('idEmp').value.trim().toUpperCase();
 let t=document.getElementById('turno').value;
 let h=document.getElementById('hora').value||new Date().toLocaleTimeString();
 let f=new Date().toLocaleDateString();
 if(!id){alert('Pon ID');return;}
 regs.push({id,turno:t,hora:h,fecha:f,sueldo:300});
 localStorage.setItem('quantum_v3',JSON.stringify(regs));
 document.getElementById('idEmp').value='';
 document.getElementById('msg').innerText='✓ '+id+' checado '+h;
 up();render();
}
function up(){
 document.getElementById('asis').textContent=regs.length;
 document.getElementById('fal').textContent=77-regs.length;
 document.getElementById('nom').textContent='$'+(regs.length*300).toLocaleString();
}
function render(){
 document.getElementById('lista').innerHTML=regs.slice(-20).reverse().map(r=>`<div class="item"><b>${r.id}</b><span>${r.fecha} ${r.hora}</span></div>`).join('');
}
function descargar(c,n){let b=new Blob([c],{type:'text/csv'});let u=URL.createObjectURL(b);let a=document.createElement('a');a.href=u;a.download=n;a.click();}
function exportar(){if(!regs.length)return alert('Sin datos');let csv='ID,TURNO,HORA,FECHA,SUELDO\n'+regs.map(r=>`${r.id},${r.turno},${r.hora},${r.fecha},${r.sueldo}`).join('\n');descargar(csv,'ASI