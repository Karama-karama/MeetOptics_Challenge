<template>
  <div class="compare">
    <h1>{{ word }}</h1>
    <h2>Compare optics</h2>
    <ul>
      <li>
        <a
          href="https://www.meetoptics.com/"
          target="_blank"
        >
          meetoptics.com
        </a>
      </li>
    </ul>
      <v-app id="inspire">

      <v-data-table
      v-model="selected"
      :headers="headers"
      :items ="products" 
      item-key ="name"
      show-select
      checkbox-color ="green"
      dense 
      class="elevation-1"
    >
       <template v-slot:headers="props">
        <tr>
          <th>
            <v-checkbox
              :input-value="props.all"
              :indeterminate="props.indeterminate"
              primary
              hide-details
              @click.stop="toggleAll"
            ></v-checkbox>
          </th>
          <th
            v-for="header in props.headers"
            :key="header.text"
            
          >
          </th>
        </tr>
      </template>
      <template v-slot:items="props">
        <tr :active="props.selected" @click="props.selected = !props.selected">
          <td>
            <v-checkbox
              :input-value="props.selected"
              primary
              hide-details
            ></v-checkbox>
          </td>
          <td>{{ props.item.name }}</td>
          <td class="text-xs-right">{{ props.item.name }}</td>
          <td class="text-xs-right">{{ props.item.Material }}</td>
          <td class="text-xs-right">{{ props.item.Diameter }}</td>
          <td class="text-xs-right">{{ props.item.delivery }}</td>
          <td class="text-xs-right">{{ props.item.coating }}</td>
          <td class="text-xs-right">{{ props.item.price }}</td>
        </tr>
      </template>
    </v-data-table> 

      </v-app>
  </div>
</template>

<script>
import HomePage from "@/components/HomePage";
import {EventBus} from'@/event-bus.js';


export default {
  name: 'ComparePage',
  data () {
    return {

      word: 'This or that ...',
     singleSelect: false,
      products : [],
      headers: [
        {
          text: 'Optics name',
          align: 'start',
          sortable: false,
          value: 'name',
        },
        { text: 'Material', value: 'Material' },
        { text: 'Diameter', value: 'Diameter' },
        { text: 'Focal', value: 'Focal length' },
        { text: 'Delivery', value: 'delivery' },
        { text: 'Coating', value: 'Coating' },
        { text: 'Price', value: 'price' },
      ]
      // selected
    }
  },
  components : {
    HomePage
  }, 
  methods : {
    // emitEnterSelect(){
    //   EventBus.$on('selected-value', (value)=> {
    //   this.products = value;
    // })
    // }
    
  },
  mounted (){
     this.products = JSON.parse(localStorage.getItem("selected"))
    console.log("From ComparePage: ",JSON.parse(localStorage.getItem("selected")) )

      
  }
}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
