const {createApp} = Vue;

const app = Vue.createApp({
    data() {
        return {
            msj: "Hola Mundo!",
            nombre: "Ramiro"
        }
    }
}).mount('#app')