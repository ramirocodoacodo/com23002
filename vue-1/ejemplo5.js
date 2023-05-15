const {createApp} = Vue;

const miComponente = {
    template: `
    <div v-on:click="cambiarNombre()" v-on:mouseout="reestablecerNombre()">
        <h1>Componente creado por <span id="nombre">{{nombre}}</span></h1>
    </div>
    `,
    data() {
        return {
            nombre: "Ramiro"
        }
    },
    methods: {
        cambiarNombre() {
            this.nombre = "Ezequiel"
        },
        reestablecerNombre() {
            this.nombre = "Ramiro"
        }
    }
}

const ejemplo5 = Vue.createApp({
    components: {
        'mi-componente': miComponente
    }
}).mount('#ejemplo5');
