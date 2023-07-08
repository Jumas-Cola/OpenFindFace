<script setup lang="ts">
import { ref, reactive, watch } from 'vue';
import ImageInput from '@/components/inputs/ImageInput.vue';

const state = reactive({
  imageData: null as null | File
});

watch(
  () => state.imageData,
  () => {
    console.log(state.imageData);
  }
);
</script>

<template>
  <div class="container d-flex justify-content-center align-items-center min-vh-100">
    <ImageInput v-model="imageData" />
  </div>
</template>
