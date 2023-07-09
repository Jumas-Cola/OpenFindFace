<script setup lang="ts">
import { reactive } from 'vue';
import ImageInput from '@/components/inputs/ImageInput.vue';
import FaceService from '@/services/FaceService';
import type ResponseData from '@/types/ResponseData';
import type Face from '@/types/Face';

const initialState: Face = {
  name: ''
};

const state = reactive({
  imageData: undefined as undefined | File,
  resetFileVariable: 0,
  data: Object.assign({}, initialState)
});

const upload = () => {
  if (state.imageData) {
    FaceService.upload(state.imageData, state.data)
      .then((res: ResponseData) => {
        state.resetFileVariable++;
        Object.assign(state.data, initialState);
      })
      .catch((err) => {
        console.log(err);
      });
  }
};
</script>

<template>
  <div class="container d-flex justify-content-center mt-5">
    <form>
      <div class="mb-3 d-flex justify-content-center">
        <ImageInput v-model="state.imageData" :reset-variable="state.resetFileVariable" />
      </div>

      <div class="mb-3">
        <label for="inputName" class="form-label">Имя</label>
        <input
          type="name"
          class="form-control"
          id="inputName"
          aria-describedby="nameHelp"
          v-model="state.data.name"
        />
        <div id="nameHelp" class="form-text">Введите имя.</div>
      </div>

      <button class="btn btn-primary" @click.prevent="upload">Загрузить</button>
    </form>
  </div>
</template>
