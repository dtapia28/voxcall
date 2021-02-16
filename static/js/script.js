$(document).ready(function(){
    $('#tipos').on('change', function(){
        var id_tipo = $(this).val();
        if(id_tipo == 1){
            document.getElementById('tipo_2').style.display = "block";
            $('#tipo_2').empty();
            $('#tipo_2').append("<option value='' selected disabled>Escoge una opción</option>");
            $('#tipo_2').append("<option value='1'>Opción Crédito</option>");
            $('#tipo_2').append("<option value='2'>Opción Producto</option>");
            $('#tipo_2').append("<option value='3'>Cuota Impaga</option>");
            $('#tipo_2').append("<option value='4'>Cambio de Clave</option>");
        } else if(id_tipo == 2) {
            document.getElementById('tipo_2').style.display = "none";
            $('#tipo_2').empty();
            $('#tipo_2').append("<option value='' selected disabled>Escoge una opción</option>");
            $('#tipo_2').append("<option value='5'>Aumento de Cupo</option>");
            $('#tipo_2').append("<option value='6'>Entrega Producto</option>");
            $('#tipo_2').append("<option value='7'>Cuota Impaga</option>");
            document.getElementById('tipo_2').style.display = "block";                
        } else if(id_tipo == 3) {
            document.getElementById('tipo_2').style.display = "none";
            $('#tipo_2').empty();
            $('#tipo_2').append("<option value='' selected disabled>Escoge una opción</option>");
            $('#tipo_2').append("<option value='8'>Hora médica</option>");
            $('#tipo_2').append("<option value='9'>Entrega resultados</option>");
            document.getElementById('tipo_2').style.display = "block";
        } else if(id_tipo == 4) {
            document.getElementById('tipo_2').style.display = "none";
            $('#tipo_2').empty();
            document.getElementById('tipo_2').style.display = "none";
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<textarea placeholder='Tu mensaje debe ir acá. Si tu mensaje llevará variables, estás deben estar entre llaves {}. Ej: {variable}' name='tipo_2' class='tipo_2_text' rows='10' cols='100'></textarea>")
            document.getElementById('muestra_texto').style.display = "block";
        }
    });
});

$(document).ready(function(){
    $('#tipo_2').on('change', function(){
        var id_mensaje = $(this).val();
        if(id_mensaje == 1){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando porque tienes un crédito preaprobado {banco} de {monto}. Este crédito está disponible hasta el {fecha}. Hasta pronto</h2>");
            document.getElementById('muestra_texto').style.display = "block";
        } else if(id_mensaje ==2){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando a nombre del banco {banco} y tenemos una excelente opción para ti. {opcion}. Esto está disponible hasta el {fecha}. Hasta pronto</h2>");
            document.getElementById('muestra_texto').style.display = "block";                
        } else if(id_mensaje ==3){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando a nombre del banco {banco} porque tienes una cuota impaga de {monto}. Por favor acercate a nuestras oficinas para regularizar tu situación. Te recordamos que la demora en el pago de la cuota genera intereses. Hasta pronto</h2>");
            document.getElementById('muestra_texto').style.display = "block";                
        } else if(id_mensaje == 4){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando a nombre del banco {banco} porque en nuestro sistema se ingresó un cambio de clave en tu cuenta. Si tú no has realizado el cambio, te solicitamos puedas entrar a tu sesión del banco para regularizar esto. Hasta pronto</h2>");
            document.getElementById('muestra_texto').style.display = "block";                  
        } else if(id_mensaje == 5){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando de {casa comercial} para informarte que hemos aumentado tu cupo para realizar compras con crédito en nuestros locales. Tu nuevo cupo es {monto}. Hasta pronto.</h2>");
            document.getElementById('muestra_texto').style.display = "block";
        } else if(id_mensaje == 6){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando de {casa comercial} para informarte que tu producto {producto} será entregado el día {fecha} en la dirección informada. Hasta pronto.</h2>");
            document.getElementById('muestra_texto').style.display = "block";
        } else if(id_mensaje == 7){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te estamos llamando de {casa comercial} porque tienes una cuota impaga de {monto}. Por favor acercate a nuestras tiendas para regularizar tu situación. Te recordamos que la demora en el pago de la cuota genera intereses. Hasta pronto.</h2>");
            document.getElementById('muestra_texto').style.display = "block";
        } else if(id_mensaje == 8){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} recuerde que tiene agendada una cita para el día {fecha} a las {hora} con {medico} {especialidad} en el {centro} ubicado en {direccion}. Hasta pronto.</h2>");
            document.getElementById('muestra_texto').style.display = "block";
        } else if(id_mensaje == 9){
            $('#muestra_texto').empty();
            $('#muestra_texto').append("<h2>Hola {nombre} te informamos que el resultado de tu {tipo} ya está disponible. Hasta pronto.</h2>");
            document.getElementById('muestra_texto').style.display = "block";
        }

    });
});

$(document).ready(function(){
    $('#tipo_2').on('change', function(){
        var id_mensaje = $(this).val();
        if(id_mensaje == 1){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1eihg_-dWvbXhWnhxW_us0JbXMvaUEQNE/view?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 2){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/19KfjTUr7CiCfXOoNPN49c1EU1fTP_zc8/view?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 3){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1tbbNxPR-_DxC6xHe5T2WjfEKvfENNc3n/view?usp=sharing'>Descargar plantilla</a>");                
        } else if(id_mensaje == 4){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://docs.google.com/spreadsheets/d/1AinbAc2jBfnB2hfipbOBVSWQ8EC_RuPGaRLDs9H_CHQ/edit?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 5){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1yp-_vV0zT7IMp1JV2tdeyDzTVIDam-2X/view?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 6){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1SuqiX5AKPzPO2OIIwUv7lEVewaVPADp8/view?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 7){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1cNB3dfoBD3sI7cV49SZ_h21hQ5V9q9eT/view?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 8){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1d5zGl3xE8QbzLcWONezGEMi_BBttoliN/view?usp=sharing'>Descargar plantilla</a>");
        } else if(id_mensaje == 9){
            $('#contiene_plantilla').empty();
            $('#contiene_plantilla').append("<a target='_blank' href='https://drive.google.com/file/d/1d92yVjTmPdTB5uBGQxGAYB9JNiqwmek1/view?usp=sharing'>Descargar plantilla</a>");
        }
    }); 
});