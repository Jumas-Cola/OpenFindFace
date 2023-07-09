<script setup lang="ts">
import { reactive } from 'vue';
import ImageInput from '@/components/inputs/ImageInput.vue';
import FaceService from '@/services/FaceService';
import type ResponseData from '@/types/ResponseData';
import type Face from '@/types/Face';
import { useVuelidate } from '@vuelidate/core';
import { required } from '@/utils/i18n-validators';

const initialState: Face = {
  name: ''
};

const state = reactive({
  imageData: undefined as undefined | File,
  resetFileVariable: 0,
  data: Object.assign({}, initialState)
});

const upload = async () => {
  const res = await v$.value.$validate();

  if (state.imageData && res) {
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

const rules = {
  name: { required }
};

const v$ = useVuelidate(rules, state.data);
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

        <div class="input-errors" v-for="error of v$.name.$errors" :key="error.$uid">
          <div class="text-danger">{{ error.$message }}</div>
        </div>
      </div>

      <button
        class="btn btn-primary"
        :class="{ disabled: !state.imageData }"
        @click.prevent="upload"
      >
        Загрузить
      </button>
    </form>
  </div>
</template>
