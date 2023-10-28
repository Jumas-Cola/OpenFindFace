<script setup lang="ts">
import { reactive } from 'vue';
import ImageInput from '@/components/inputs/ImageInput.vue';
import FaceService from '@/services/FaceService';
import FaceCardItem from '@/components/face/FaceCardItem.vue';
import type ResponseData from '@/types/ResponseData';
import type Face from '@/types/Face';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const state = reactive({
  imageData: undefined as File | undefined,
  searchResult: null as null | Array<Face>,
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
      <button
        class="btn btn-primary"
        :class="{ disabled: !state.imageData }"
        @click.prevent="search"
      >
        {{ t('search') }}
      </button>
    </div>

    <div class="w-100 d-flex justify-content-center mt-3">
      <div v-if="state.searchResult && !state.notFound" class="w-50">
        <FaceCardItem
          v-for="face in state.searchResult"
          :face-data="face"
          :key="face.id"
          class="w-100"
        />
      </div>

      <div v-if="state.notFound" class="d-flex justify-content-center">{{ t('notFound') }}</div>
    </div>
  </div>
</template>
