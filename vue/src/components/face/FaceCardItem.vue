<script setup lang="ts">
const props = defineProps({
  faceData: {
    type: Object,
    required: true
  }
});
</script>

<template>
  <table class="table">
    <tbody>
      <tr>
        <th class="fw-bold" scope="row">Фото</th>
        <td class="d-flex justify-content-center">
          <img :src="`/${props.faceData.image}`" width="100" height="100" />
        </td>
      </tr>
      <tr>
        <th class="fw-bold" scope="row">Имя</th>
        <td class="text-center">{{ props.faceData.name }}</td>
      </tr>
    </tbody>
  </table>
</template>
