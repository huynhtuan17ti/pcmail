<template>
  <div class="q-pa-lg">
    <q-table
      title="Help table"
      bordered
      :rows="rows"
      :columns="columns"
      row-key="name"
      separator="vertical"
      :rows-per-page-options="[0]"
    />
  </div>
</template>

<script>
import { computed, defineComponent } from 'vue';
import {
  message,
  sending_format,
  detail,
  response,
  message_title,
} from 'src/constants/gmail';
import { extensions } from 'src/constants/extenstions';

export default defineComponent({
  setup() {
    const columns = [
      {
        name: 'controller',
        label: 'Controller',
        align: 'left',
        field: 'controller',
      },
      {
        name: 'detail',
        label: 'Details',
        align: 'left',
        field: 'detail',
      },
      {
        name: 'format',
        label: 'Email format',
        align: 'left',
        field: 'format',
      },
      {
        name: 'response',
        label: 'Response details',
        align: 'left',
        field: 'response',
      },
    ];

    const rows = computed(() => {
      var row_array = [];
      for (var i = 0; i < extensions.length; i++) {
        var controller_name = extensions[i];
        row_array.push({
          controller: message_title[controller_name],
          detail: detail[controller_name],
          format:
            message[controller_name] +
            ' ' +
            (sending_format[controller_name]
              ? sending_format[controller_name]
              : ' '),
          response: response[controller_name],
        });
      }
      return row_array;
    });

    return {
      columns,
      rows,
    };
  },
});
</script>
