$(document).ready(function(){
    const Toast1 = Swal.mixin({
        toast: true,
        position: 'top-start',
        showConfirmButton: false,
        timer: 6000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.onmouseenter = Swal.stopTimer;
            toast.onmouseleave = Swal.resumeTimer;
        }
    });

    Toast1.fire({
        icon: 'success',
        title: 'Signed in successfully',
    });
});

$(document).ready(function(){
    const Toast2 = Swal.mixin({
        toast: true,
        position: 'top-end',
        showConfirmButton: false,
        timer: 6000,
        timerProgressBar: true,
        didOpen: (toast) => {
            toast.onmouseenter = Swal.stopTimer;
            toast.onmouseleave = Swal.resumeTimer;
        }
    });

    Toast2.fire({
        icon: 'success',
        title: 'Signed in successfully',
    });
});