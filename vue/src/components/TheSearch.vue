<script setup lang="ts">
import { reactive } from 'vue';
import ImageInput from '@/components/inputs/ImageInput.vue';
import FaceService from '@/services/FaceService';
import FaceCardItem from '@/components/face/FaceCardItem.vue';
import type ResponseData from '@/types/ResponseData';
import type Face from '@/types/Face';

const state = reactive({
  imageData: undefined as File | undefined,
  searchResult: null as null | Face,
  notFound: false as boolean
});

const search = () => {
  state.notFound = false;
  state.searchResult = null;
  if (state.imageData) {
    FaceService.search(state.imageData)
      .then((res: ResponseData) => {
        state.searchResult = res.data;
      })
      .catch((err) => {
        state.notFound = true;
      });
  }
};
</script>

<template>
  <div class="container mt-5">
    <div class="w-100 d-flex justify-content-center">
      <ImageInput v-model="state.imageData" />
    </div>

    <div class="w-100 d-flex justify-content-center mt-3">
      <FaceCardItem
        v-if="state.searchResult && !state.notFound"
        :face-data="state.searchResult"
        class="w-50"
      />
      <div v-if="state.notFound" class="d-flex justify-content-center">Ничего не найдено</div>
    </div>

    <div class="w-100 d-flex justify-content-center mt-3">
      <button class="btn btn-primary" @click.prevent="search">Поиск</button>
    </div>
  </div>
</template>
