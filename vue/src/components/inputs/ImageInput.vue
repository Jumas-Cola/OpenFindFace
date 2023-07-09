<script setup lang="ts">
import { ref, reactive, watch } from 'vue';

const props = defineProps({
  modelValue: File,
  resetVariable: Number
});

const state = reactive({
  imageData: '' as string | ArrayBuffer,
  imageName: null as string | null,
  draggedOver: false as boolean
});

const emits = defineEmits(['update:modelValue']);

const fileInput = ref<HTMLInputElement | null>(null);

const onSelectFile = () => {
  const input = fileInput.value;
  const files: FileList = input?.files!;
  handleFiles(files);
};

const onFileDragged = (e: DragEvent) => {
  const files = e?.dataTransfer?.files!;
  handleFiles(files);
};

const handleFiles = (files: FileList) => {
  if (files && files[0]) {
    const reader = new FileReader();
    reader.onload = (e) => {
      state.imageData = e?.target?.result!;
    };
    reader.readAsDataURL(files[0]);
    state.imageName = files[0].name;
    emits('update:modelValue', files[0]);
  }
};

const chooseImage = () => {
  fileInput?.value?.click();
};

watch(
  () => props.resetVariable,
  () => {
    state.imageData = '';
    state.imageName = null;
  }
);
</script>

<template>
  <div>
    <div
      class="base-image-input d-block rounded"
      :class="{ 'on-drag-above': state.draggedOver }"
      :style="{ 'background-image': `url(${state.imageData})` }"
      @drop.prevent="onFileDragged"
      @dragenter.prevent="state.draggedOver = true"
      @dragover.prevent="state.draggedOver = true"
      @dragleave.prevent="state.draggedOver = false"
      @click="chooseImage"
    >
      <span
        v-if="!state.imageData"
        class="placeholder w-100 h-100 d-flex justify-content-center align-items-center text-muted text-center rounded p-5"
      >
        Загрузите фото для поиска или перетащите его сюда
      </span>
      <input
        class="d-none"
        ref="fileInput"
        type="file"
        @input="onSelectFile"
        accept=".pdf,.jpg,.jpeg,.png"
      />
    </div>

    <div v-if="state.imageName" class="d-flex justify-content-center align-items-center">
      Файл:
      {{ state.imageName.length > 20 ? state.imageName.substring(0, 20) + '...' : state.imageName }}
    </div>
  </div>
</template>

<style scoped>
.base-image-input {
  width: 200px;
  height: 200px;
  cursor: pointer;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: center center;
}
.placeholder {
  background: #f0f0f0;
  cursor: pointer;
}
.placeholder:hover {
  background: #e0e0f0;
}
.on-drag-above {
  background-color: #0d6efd;
}
</style>
