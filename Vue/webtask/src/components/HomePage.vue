<template>
  <div class="home">
    <h1>{{ msg }}</h1>
    <h2>Home page</h2>
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
    <p> <router-link to= "./ComparePage">Compare Products</router-link>  </p>
      <v-app id="inspire">
      <v-data-table
      v-model="selected"
      @input="emitEnterSelect"
      :selected ="$emit('emitEnterSelect')"
      :headers="headers"
      :items="desserts"
      item-key ="name"
      show-select
      checkbox-color ="$emit('emitEnterSelect')"
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
               v-model = checkbox
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
import optics from "../../../../../Internship/optics.json"
import ComparePage from "@/components/ComparePage"
import {EventBus} from'@/event-bus.js'
export default {
  name: 'HomePage',
  data () {
    return {
      selected: [ ],
      msg: 'MEETOPTICS',
      singleSelect: false,
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

      ],
      desserts: optics, 
    }
    
  },
   methods : {
     async emitEnterSelect() {
       await new Promise(r => setTimeout(r));
        console.log("Item selected",this.selected.map(e => e.name));  
       console.log("From home page ", this.selected)
       this.$emit('selected-value', this.selected);
       localStorage.setItem('selected',JSON.stringify(this.selected))
      
    
  },

   },
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
