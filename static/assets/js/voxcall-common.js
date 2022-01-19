function AgregarRegistro() {
    //event.preventDefault();
    var tipo = $('#tipo2').val();

    if (tipo == "1") {
        var nombre = $('#nombre').val();
        var banco = $('#banco').val();
        var monto = $('#monto').val();
        var fecha = formatoFecha($('#fecha').val());
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        //alert(cantidad);
        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (banco == "" || banco == null) {
            alert('Ingrese el banco');
            return;
        }
        if (monto == "" || monto == null || monto == 0) {
            alert('Ingrese el monto');
            return;
        }
        if (fecha == "" || fecha == null) {
            alert('Ingrese la fecha');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var prueba_fecha = fecha.slice(6,10)+"-"+fecha.slice(3,5)+"-"+fecha.slice(0,2);

        var registro = '<tr id="'+nro+'"><td><input type="text" name=nombre'+i+' class="form-control" value='+nombre+
        '></td><td><input type="text" name=banco'+i+' class="form-control" value='+banco+
        '></td><td><input type="number" name=monto'+i+' class="form-control" value='+monto+
        '></td><td><input type="date" name=fecha'+i+' class="form-control" value='+prueba_fecha+
        '></td><td><input type="tel" name=phone'+i+' class="form-control" value='+telefono+
        '></td><td class="text-center"><button onclick="EliminarRegistro('+nro+
        ')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo == "2"){

        var nombre = $('#nombre').val();
        var banco = $('#banco').val();
        var opcion = $('#opcion').val();
        var fecha = formatoFecha($('#fecha').val());
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (banco == "" || banco == null) {
            alert('Ingrese el banco');
            return;
        }
        if (opcion == "" || opcion == null) {
            alert('Ingrese la opción');
            return;
        }
        if (fecha == "" || fecha == null) {
            alert('Ingrese la fecha');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=banco'+i+'>'+banco+'</td><td name=opcion'+i+'>'+opcion+'</td><td name=fecha'+i+'>'+fecha+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo == "3"){
        var nombre = $('#nombre').val();
        var banco = $('#banco').val();
        var monto = $('#monto').val();
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (banco == "" || banco == null) {
            alert('Ingrese el banco');
            return;
        }
        if (monto == "" || monto == null || monto == 0) {
            alert('Ingrese el monto');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=banco'+i+'>'+banco+'</td><td name=monto'+i+'>'+monto+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo == "4"){
        var nombre = $('#nombre').val();
        var banco = $('#banco').val();
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (banco == "" || banco == null) {
            alert('Ingrese el banco');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=banco'+i+'>'+banco+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo =="5"){
        var nombre = $('#nombre').val();
        var casa_comercial = $('#casa_comercial').val();
        var monto = $('#monto').val();
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (casa_comercial == "" || casa_comercial == null) {
            alert('Ingrese la casa comercial');
            return;
        }
        if (monto == "" || monto == null || monto == 0) {
            alert('Ingrese el monto');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=casa_comercial'+i+'>'+casa_comercial+'</td><td name=monto'+i+'>'+monto+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo == "6"){
        var nombre = $('#nombre').val();
        var casa_comercial = $('#casa_comercial').val();
        var producto = $('#producto').val();
        var fecha = formatoFecha($('#fecha').val());
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (casa_comercial == "" || casa_comercial == null) {
            alert('Ingrese la casa comercial');
            return;
        }
        if (producto == "" || producto == null) {
            alert('Ingrese el producto');
            return;
        }
        if (fecha == "" || fecha == null) {
            alert('Ingrese la fecha');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=casa_comercial'+i+'>'+casa_comercial+'</td><td name=producto'+i+'>'+producto+'</td><td name=fecha'+i+'>'+fecha+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo == "7"){
        var nombre = $('#nombre').val();
        var casa_comercial = $('#casa_comercial').val();
        var monto = $('#monto').val();
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (casa_comercial == "" || casa_comercial == null) {
            alert('Ingrese la casa comercial');
            return;
        }
        if (monto == "" || monto == null || monto == 0) {
            alert('Ingrese el monto');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=casa_comercial'+i+'>'+casa_comercial+'</td><td name=monto'+i+'>'+monto+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);

        LimpiarRegistro();
    } else if(tipo == "8"){
        var nombre = $('#nombre').val();
        var fecha = formatoFecha($('#fecha').val());
        var hora = $('#hora').val();
        var medico = $('#medico').val();
        var especialidad = $('#especialidad').val();
        var centro = $('#centro').val();
        var direccion = $('#direccion').val();
        var telefono = $('#telefono').val();
        var cantidad = $('#ultima').val();
        var nFilas = $("#tablaRegistros tbody tr").length;

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (fecha == "" || fecha == null) {
            alert('Ingrese la fecha');
            return;
        }
        if (hora == "" || hora == null) {
            alert('Ingrese la hora');
            return;
        }
        if (medico == "" || medico == null) {
            alert('Ingrese el medico');
            return;
        }
        if (especialidad == "" || especialidad == null) {
            alert('Ingrese la especialidad');
            return;
        }
        if (centro == "" || centro == null) {
            alert('Ingrese el centro');
            return;
        }
        if (direccion == "" || direccion == null) {
            alert('Ingrese la dirección');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=fecha'+i+'>'+fecha+'</td><td name=hora'+i+'>'+hora+'</td><td name=medico'+i+'>'+medico+'</td><td name=especialidad'+i+'>'+especialidad+'</td><td name=centro'+i+'>'+centro+'</td><td name=direccion'+i+'>'+direccion+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);
    } else if(tipo == "9"){
        var nombre = $('#nombre').val();
        var tipo = $('#tipo').val();
        var telefono = $('#telefono').val();

        var i;
        var nro;

        if (nombre == "" || nombre == null) {
            alert('Ingrese el nombre');
            return;
        }
        if (tipo == "" || tipo == null) {
            alert('Ingrese el tipo');
            return;
        }
        if (telefono == "" || telefono == null) {
            alert('Ingrese el teléfono');
            return;
        } else if (telefono != "" && telefono != null) {
            if (telefono.length != 11) {
                alert("El telefóno debe tener once (11) dígitos");
                $('#telefono').val("");
                $('#telefono').focus();
                return (false);
            }
        }

        i = parseInt(cantidad) + parseInt(1);
        nro = 'nro'+i;
        $('#ultima').val(i);

        var registro = '<tr id="'+nro+'"><td name=nombre'+i+'>'+nombre+'</td><td name=tipo'+i+'>'+tipo+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

        // $('#tablaRegistros tbody').append(registro);
        $('#tablaRegistros').DataTable().row.add($(registro)).draw();

        var nFilas = $("#tablaRegistros tbody tr").length;
        var cantidad = [];
        for (let index = 0; index < nFilas; index++) {
            cantidad.push(index);
        }

        cantidad = cantidad.join(', ');
        cantidad = "["+cantidad+"]";

        $('input[name=cantidad]').val(cantidad);
    } else if(tipo == "0"){
        var variables = $('#variables').val();

        if (variables != 0){
            numero = parseInt(variables);
            numero2 = numero-1;
            switch (numero) {
                case 1:
                    var elemento = $('#variable_0').val();
                    var telefono = $('#telefono').val();
                    var cantidad = $('#ultima').val();
                    var nFilas = $("#tablaRegistros tbody tr").length;

                    var i;
                    var nro;

                    if (elemento == ""||elemento == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (telefono == "" || telefono == null) {
                        alert('Ingrese el teléfono');
                        return;
                    } else if (telefono != "" && telefono != null) {
                        if (telefono.length != 11) {
                            alert("El telefóno debe tener once (11) dígitos");
                            $('#telefono').val("");
                            $('#telefono').focus();
                            return (false);
                        }
                    }
                    i = parseInt(cantidad) + parseInt(1);
                    nro = 'nro'+i;
                    $('#ultima').val(i);

                    var registro = '<tr id="'+nro+'"><td><input type="text" name=variable_'+i+'_'+numero2+
                    ' id=variable_'+i+'_'+numero2+' value='+elemento+
                    ' class="form-control"></td><td><input type="text" id=phone'+i+' name=phone'+i+
                    ' value='+telefono+
                    ' class="form-control"></td><td class="text-center"><button onclick="EliminarRegistro('+nro+
                    ')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

                    // $('#tablaRegistros tbody').append(registro);
                    $('#tablaRegistros').DataTable().row.add($(registro)).draw();

                    var nFilas = $("#tablaRegistros tbody tr").length;
                    var cantidad = [];
                    for (let index = 0; index < nFilas; index++) {
                        cantidad.push(index);
                    }

                    cantidad = cantidad.join(', ');
                    cantidad = "["+cantidad+"]";

                    $('input[name=cantidad]').val(cantidad);
                    break;
                case 2:
                    var elemento = $('#variable_0').val();
                    var elemento1 = $('#variable_1').val();
                    var telefono = $('#telefono').val();
                    var cantidad = $('#ultima').val();
                    var nFilas = $("#tablaRegistros tbody tr").length;

                    var i;
                    var nro;

                    if (elemento == ""||elemento == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento1 == ""||elemento1 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (telefono == "" || telefono == null) {
                        alert('Ingrese el teléfono');
                        return;
                    } else if (telefono != "" && telefono != null) {
                        if (telefono.length != 11) {
                            alert("El telefóno debe tener once (11) dígitos");
                            $('#telefono').val("");
                            $('#telefono').focus();
                            return (false);
                        }
                    }
                    i = parseInt(cantidad) + parseInt(1);
                    nro = 'nro'+i;
                    $('#ultima').val(i);

                    var registro = '<tr id="'+nro+'"><td><input type="text" name=variable_'+i+'_'+(numero2-1)+
                    ' id=variable_'+i+'_'+(numero2-1)+' value='+elemento+
                    ' class="form-control"></td><td><input type="text" name=variable_'+i+'_'+numero2+
                    ' id=variable_'+i+'_'+numero2+' value='+elemento1+
                    ' class="form-control"></td><td><input type="text" id=phone'+i+' name=phone'+i+
                    ' value='+telefono+
                    ' class="form-control"></td><td class="text-center"><button onclick="EliminarRegistro('+nro+
                    ')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

                    // $('#tablaRegistros tbody').append(registro);
                    $('#tablaRegistros').DataTable().row.add($(registro)).draw();

                    var nFilas = $("#tablaRegistros tbody tr").length;
                    var cantidad = [];
                    for (let index = 0; index < nFilas; index++) {
                        cantidad.push(index);
                    }

                    cantidad = cantidad.join(', ');
                    cantidad = "["+cantidad+"]";

                    $('input[name=cantidad]').val(cantidad);
                    break;
                case 3:
                    var elemento = $('#variable_0').val();
                    var elemento1 = $('#variable_1').val();
                    var elemento2 = $('#variable_2').val();
                    var telefono = $('#telefono').val();
                    var cantidad = $('#ultima').val();
                    var nFilas = $("#tablaRegistros tbody tr").length;

                    var i;
                    var nro;

                    if (elemento == ""||elemento == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento1 == ""||elemento1 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento2 == ""||elemento2 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (telefono == "" || telefono == null) {
                        alert('Ingrese el teléfono');
                        return;
                    } else if (telefono != "" && telefono != null) {
                        if (telefono.length != 11) {
                            alert("El telefóno debe tener once (11) dígitos");
                            $('#telefono').val("");
                            $('#telefono').focus();
                            return (false);
                        }
                    }
                    i = parseInt(cantidad) + parseInt(1);
                    nro = 'nro'+i;
                    $('#ultima').val(i);

                    var registro = '<tr id="'+nro+'"><td><input type="text" name=variable_'+i+'_'+(numero2-2)+
                    ' id=variable_'+i+'_'+(numero2-2)+' value='+elemento+
                    ' class="form-control"></td><td><input type="text" name=variable_'+i+'_'+(numero2-1)+
                    ' id=variable_'+i+'_'+(numero2-1)+' value='+elemento1+
                    ' class="form-control"></td><td><input type="text" name=variable_'+i+'_'+(numero2)+
                    ' id=variable_'+i+'_'+(numero2)+' value='+elemento2+
                    ' class="form-control"></td><td><input type="text" id=phone'+i+' name=phone'+i+
                    ' value='+telefono+
                    ' class="form-control"></td><td class="text-center"><button onclick="EliminarRegistro('+nro+
                    ')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

                    // $('#tablaRegistros tbody').append(registro);
                    $('#tablaRegistros').DataTable().row.add($(registro)).draw();

                    var nFilas = $("#tablaRegistros tbody tr").length;
                    var cantidad = [];
                    for (let index = 0; index < nFilas; index++) {
                        cantidad.push(index);
                    }

                    cantidad = cantidad.join(', ');
                    cantidad = "["+cantidad+"]";

                    $('input[name=cantidad]').val(cantidad);
                    break;
                case 4:
                    var elemento = $('#variable_0').val();
                    var elemento1 = $('#variable_1').val();
                    var elemento2 = $('#variable_2').val();
                    var elemento3 = $('#variable_3').val();
                    var telefono = $('#telefono').val();
                    var cantidad = $('#ultima').val();
                    var nFilas = $("#tablaRegistros tbody tr").length;

                    var i;
                    var nro;

                    if (elemento == ""||elemento == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento1 == ""||elemento1 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento2 == ""||elemento2 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento3 == ""||elemento3 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (telefono == "" || telefono == null) {
                        alert('Ingrese el teléfono');
                        return;
                    } else if (telefono != "" && telefono != null) {
                        if (telefono.length != 11) {
                            alert("El telefóno debe tener once (11) dígitos");
                            $('#telefono').val("");
                            $('#telefono').focus();
                            return (false);
                        }
                    }
                    i = parseInt(cantidad) + parseInt(1);
                    nro = 'nro'+i;
                    $('#ultima').val(i);

                    var registro = '<tr id="'+nro+'"><td><input type="text" name=variable_'+i+'_'+(numero2-3)+
                    ' id=variable_'+i+'_'+(numero2-3)+' value='+elemento+
                    ' class="form-control"></td><td><input type="text" name=variable_'+i+'_'+(numero2-2)+
                    ' id=variable_'+i+'_'+(numero2-2)+' value='+elemento1+
                    ' class="form-control"></td><td><input type="text" name=variable_'+i+'_'+(numero2-1)+
                    ' id=variable_'+i+'_'+(numero2-1)+' value='+elemento2+
                    ' class="form-control"></td><td><input type="text" name=variable_'+i+'_'+(numero2)+
                    ' id=variable_'+i+'_'+(numero2)+' value='+elemento3+
                    ' class="form-control"></td><td><input type="text" id=phone'+i+' name=phone'+i+
                    ' value='+telefono+
                    ' class="form-control"></td><td class="text-center"><button onclick="EliminarRegistro('+nro+
                    ')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

                    // $('#tablaRegistros tbody').append(registro);
                    $('#tablaRegistros').DataTable().row.add($(registro)).draw();
                    
                    var nFilas = $("#tablaRegistros tbody tr").length;
                    var cantidad = [];
                    for (let index = 0; index < nFilas; index++) {
                        cantidad.push(index);
                    }

                    cantidad = cantidad.join(', ');
                    cantidad = "["+cantidad+"]";

                    $('input[name=cantidad]').val(cantidad);
                    break;
                case 5:
                    var elemento = $('#variable_0').val();
                    var elemento1 = $('#variable_1').val();
                    var elemento2 = $('#variable_2').val();
                    var elemento3 = $('#variable_3').val();
                    var elemento4 = $('#variable_4').val();
                    var telefono = $('#telefono').val();
                    var cantidad = $('#ultima').val();
                    var nFilas = $("#tablaRegistros tbody tr").length;

                    var i;
                    var nro;

                    if (elemento == ""||elemento == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento1 == ""||elemento1 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento2 == ""||elemento2 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento3 == ""||elemento3 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento4 == ""||elemento4 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (telefono == "" || telefono == null) {
                        alert('Ingrese el teléfono');
                        return;
                    } else if (telefono != "" && telefono != null) {
                        if (telefono.length != 11) {
                            alert("El telefóno debe tener once (11) dígitos");
                            $('#telefono').val("");
                            $('#telefono').focus();
                            return (false);
                        }
                    }
                    i = parseInt(cantidad) + parseInt(1);
                    nro = 'nro'+i;
                    $('#ultima').val(i);

                    var registro = '<tr id="'+nro+'"><td name=variable_'+i+'_'+0+'>'+elemento+'</td><td name=variable_'+i+'_'+1+'>'+elemento1+'</td><td name=variable_'+i+
                    '_'+2+'>'+elemento2+'</td><td name=variable_'+i+'_'+3+'>'+elemento3+'</td><td name=variable_'+i+'_'+4+'>'+elemento4+'</td><td name=phone'+i+'>'+
                    telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

                    // $('#tablaRegistros tbody').append(registro);
                    $('#tablaRegistros').DataTable().row.add($(registro)).draw();

                    var nFilas = $("#tablaRegistros tbody tr").length;
                    var cantidad = [];
                    for (let index = 0; index < nFilas; index++) {
                        cantidad.push(index);
                    }

                    cantidad = cantidad.join(', ');
                    cantidad = "["+cantidad+"]";

                    $('input[name=cantidad]').val(cantidad);
                    break;
                case 6:
                    var elemento = $('#variable_0').val();
                    var elemento1 = $('#variable_1').val();
                    var elemento2 = $('#variable_2').val();
                    var elemento3 = $('#variable_3').val();
                    var elemento4 = $('#variable_4').val();
                    var elemento5 = $('#variable_5').val();
                    var telefono = $('#telefono').val();
                    var cantidad = $('#ultima').val();
                    var nFilas = $("#tablaRegistros tbody tr").length;

                    var i;
                    var nro;

                    if (elemento == ""||elemento == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento1 == ""||elemento1 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento2 == ""||elemento2 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento3 == ""||elemento3 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento4 == ""||elemento4 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (elemento5 == ""||elemento5 == null) {
                        alert('Ingrese variable');
                        return;
                    }
                    if (telefono == "" || telefono == null) {
                        alert('Ingrese el teléfono');
                        return;
                    } else if (telefono != "" && telefono != null) {
                        if (telefono.length != 11) {
                            alert("El telefóno debe tener once (11) dígitos");
                            $('#telefono').val("");
                            $('#telefono').focus();
                            return (false);
                        }
                    }
                    i = parseInt(cantidad) + parseInt(1);
                    nro = 'nro'+i;
                    $('#ultima').val(i);

                    var registro = '<tr id="'+nro+'"><td name=variable_'+i+'_'+0+'>'+elemento+'</td><td name=variable_'+i+'_'+1+'>'+elemento1+'</td><td name=variable_'+i+
                    '_'+2+'>'+elemento2+'</td><td name=variable_'+i+'_'+3+'>'+elemento3+'</td><td name=variable_'+i+'_'+4+'>'+elemento4+'</td><td name=variable_'+i+
                    '_'+5+'>'+elemento5+'</td><td name=phone'+i+'>'+telefono+'</td><td class="text-center"><button onclick="EliminarRegistro('+nro+')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';

                    // $('#tablaRegistros tbody').append(registro);
                    $('#tablaRegistros').DataTable().row.add($(registro)).draw();

                    var nFilas = $("#tablaRegistros tbody tr").length;
                    var cantidad = [];
                    for (let index = 0; index < nFilas; index++) {
                        cantidad.push(index);
                    }

                    cantidad = cantidad.join(', ');
                    cantidad = "["+cantidad+"]";

                    $('input[name=cantidad]').val(cantidad);
                    break;
                default:
                    break;
            }
        } else {
            var telefono = $('#telefono').val();
            var cantidad = $('#ultima').val();
            var nFilas = $("#tablaRegistros tbody tr").length;

            var i; 
            var nro;

            if (telefono == "" || telefono == null) {
                alert('Ingrese el teléfono');
                return;
            } else if (telefono != "" && telefono != null) {
                if (telefono.length != 11) {
                    alert("El telefóno debe tener once (11) dígitos");
                    $('#telefono').val("");
                    $('#telefono').focus();
                    return (false);
                }
            }
            i = parseInt(cantidad) + parseInt(1);
            nro = 'nro'+i;
            $('#ultima').val(i);

            var registro = '<tr id="'+nro+'"><td><input type="text" id=phone'+i+' name=phone'+i+
            ' value='+telefono+
            ' class="form-control"></td><td class="text-center"><button onclick="EliminarRegistro('+nro+
            ')" title="Eliminar Registro" class="btn btn-danger btn-sm"><i class="fa fa-trash-alt"></i></button></td></tr>';        
            
            // $('#tablaRegistros tbody').append(registro);
            $('#tablaRegistros').DataTable().row.add($(registro)).draw();

            var nFilas = $("#tablaRegistros tbody tr").length;
            var cantidad = [];
            for (let index = 0; index < nFilas; index++) {
                cantidad.push(index);
            }
                
            cantidad = cantidad.join(', ');
            cantidad = "["+cantidad+"]";
                
            $('input[name=cantidad]').val(cantidad);            
        }
    }
}

function GuardarRegistros() {
    var registrosJson = [];

    $('#tablaRegistros tbody tr').each(function () {
        var nombre = $(this).find("td").eq(0).html();
        var banco = $(this).find("td").eq(1).html();
        var monto = $(this).find("td").eq(2).html();
        var fecha = $(this).find("td").eq(3).html();
        var telefono = $(this).find("td").eq(4).html();

        item = {};
        item["nombre"] = nombre;
        item["banco"] = banco;
        item["monto"] = monto;
        item["fecha"] = fecha;
        item["telefono"] = telefono;

        registrosJson.push(item);
    });

    /* SE CAPTURAN Y MUESTRAN LOS DATOS CARGADOS EN LA TABLA */
    console.log(registrosJson);
}

function EliminarRegistro(idRow) {
    var cantidad = $('#ultima').val();
    var idDelete = idRow.getAttribute('id');
    
    // $("#tablaRegistros tbody").find(idRow).remove();
    $('#tablaRegistros').DataTable().row($('#'+idDelete)).remove().draw();

    var nFilas = $("#tablaRegistros tbody tr").length;
    var cantidad = [];
    for (let index = 0; index < nFilas; index++) {
        cantidad.push(index);
    }

    cantidad = cantidad.join(', ');
    cantidad = "["+cantidad+"]";

    $('input[name=cantidad]').val(cantidad);

    cantidad = parseInt(cantidad);
}

function LimpiarRegistro() {
    $('#nombre').val("");
    $('#banco').val("");
    $('#telefono').val("");
    $('#monto').val("");
    $('#fecha').val("");
    $('#nombre').focus();
}

function formatoFecha(fecha){
    return fecha.replace(/^(\d{4})-(\d{2})-(\d{2})$/g,'$3/$2/$1');
}
